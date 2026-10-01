"""Dasbor analitik perkotaan — menyatukan hasil notebook 04–12.

Jalankan dari akar proyek:  streamlit run app/dasbor.py
Kota mengikuti city_config.json (atau variabel lingkungan KOTA_CONFIG).
"""
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pydeck as pdk
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from kota import CFG, PROC  # noqa: E402

st.set_page_config(page_title=f"Dasbor {CFG['name']}", layout="wide")


@st.cache_data
def baca(nama, layer):
    f = PROC / nama
    if not f.exists():
        return None
    return gpd.read_file(f, layer=layer).to_crs(4326)


@st.cache_data
def baca_csv(nama):
    f = PROC / nama
    return pd.read_csv(f) if f.exists() else None


def peta(gdf, kolom, label, zoom=10.5, skala=None, garis=False, baik_tinggi=False):
    """Warna hijau → merah. baik_tinggi=True membalik skala untuk ukuran yang makin tinggi makin baik (akses)."""
    g = gdf.copy()
    v = g[kolom].astype(float)
    lo, hi = skala or (v.quantile(0.02), v.quantile(0.98))
    t = ((v - lo) / (hi - lo)).clip(0, 1).fillna(0)
    if baik_tinggi:
        t = 1 - t
    g["_r"] = (255 * t).astype(int)
    g["_g"] = (200 * (1 - t)).astype(int)
    g["_b"] = (80 * (1 - t)).astype(int)
    g["_nilai"] = v.round(3)
    rendah, tinggi = ("merah", "hijau") if baik_tinggi else ("hijau", "merah")
    st.caption(f"{kolom}: {rendah} = {lo:,.2f} atau kurang · {tinggi} = {hi:,.2f} atau lebih")
    layer = pdk.Layer("GeoJsonLayer", g.__geo_interface__, pickable=True, opacity=0.75,
                      get_fill_color="[properties._r, properties._g, properties._b]",
                      get_line_color="[properties._r, properties._g, properties._b]" if garis else [80, 80, 80],
                      line_width_min_pixels=2 if garis else 0.5)
    view = pdk.ViewState(latitude=CFG["lat"], longitude=CFG["lon"], zoom=zoom)
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view, map_style=None,
                             tooltip={"text": f"{{{label}}}\n{kolom}: {{_nilai}}"}))


st.sidebar.title(CFG["name"])
st.sidebar.caption(f"{CFG['province']} · EPSG:{CFG['epsg_utm']}")
halaman = st.sidebar.radio("Topik", ["Ringkasan", "Bentuk kota", "KDB & zonasi", "Akses puskesmas",
                                      "Perubahan lahan", "Risiko pesisir", "Mobilitas (sintetis)"])

kel = baca("morfologi.gpkg", "kelurahan")

if halaman == "Ringkasan":
    st.title(f"Analitik Perkotaan — {CFG['name']}")
    c = st.columns(4)
    c[0].metric("Kelurahan", len(kel))
    c[1].metric("Bangunan dalam kelurahan", f"{int(kel['n_bangunan'].sum()):,}".replace(",", "."))
    eks = baca("ekspansi_terbangun.gpkg", "kelurahan")
    if eks is not None:
        c[2].metric("Terbangun 2024 (ha)", f"{eks['ha_terbangun_2024'].sum():,.0f}".replace(",", "."),
                    f"+{eks['ha_baru'].sum():,.0f} ha sejak 2020".replace(",", "."))
    ris = baca("risiko_pesisir.gpkg", "kelurahan")
    if ris is not None:
        c[3].metric("Kelurahan risiko pesisir tertinggi", ris.sort_values("indeks_risiko").iloc[-1]["kelurahan"])
    st.markdown("Sumber: OpenStreetMap (ODbL), GHLC (OpenGeoHub), Copernicus DEM, Landsat (USGS). "
                "Zonasi, lalu lintas, dan ojol **sintetis**.")

elif halaman == "Bentuk kota":
    kolom = st.selectbox("Metrik", ["bangunan_per_ha", "rasio_tutupan", "tapak_median_m2", "blok_median_m2"])
    peta(kel, kolom, "kelurahan")
    st.dataframe(kel.drop(columns="geometry").sort_values(kolom, ascending=False)
                 [["kelurahan", "kecamatan", kolom]].head(15), hide_index=True)

elif halaman == "KDB & zonasi":
    st.warning("Batas zonasi SINTETIS dan blok bukan persil: peta ini alat penyaring, bukan bukti pelanggaran.")
    blok = baca("kdb_blok.gpkg", "blok")
    zona = st.multiselect("Zona", sorted(blok["zona"].unique()), default=sorted(blok["zona"].unique()))
    b = blok[blok["zona"].isin(zona)]
    hanya = st.toggle("Hanya yang melampaui jelas", value=True)
    if hanya:
        b = b[b["status_kdb"] == "melampaui jelas"]
    st.caption(f"{len(b)} blok ditampilkan")
    peta(b, "kdb", "zona", zoom=11, skala=(0.3, 1.0))

elif halaman == "Akses puskesmas":
    g = kel.merge(baca_csv("akses_puskesmas_kelurahan.csv"), on="id")
    cara = st.radio("Ukuran jarak", ["jaringan_15mnt", "lurus_15mnt"], horizontal=True)
    peta(g, cara, "kelurahan", skala=(0, 1), baik_tinggi=True)
    st.caption("Bagian bangunan dalam 15 menit berjalan (1.125 m) dari puskesmas.")

elif halaman == "Perubahan lahan":
    eks = baca("ekspansi_terbangun.gpkg", "kelurahan")
    seri = baca_csv("ghlc_seri_2020_2024.csv")
    if seri is not None:
        st.line_chart(seri.set_index(seri.columns[0]).T)
    peta(eks, "ha_baru", "kelurahan")
    st.caption("Lahan terbangun baru 2020→2024 (ha), dari GHLC 30 m.")

elif halaman == "Risiko pesisir":
    st.warning("DSM bukan DTM, tanpa tanggul/pompa, laju penurunan tanah ilustratif.")
    ris = baca("risiko_pesisir.gpkg", "kelurahan")
    peta(ris, "indeks_risiko", "kelurahan", skala=(0, 0.7))
    st.dataframe(ris.drop(columns="geometry").sort_values("indeks_risiko", ascending=False)
                 [["kelurahan", "kecamatan", "bagian_genang", "indeks_risiko"]].head(10).round(3), hide_index=True)

elif halaman == "Mobilitas (sintetis)":
    st.error("Semua data di halaman ini SINTETIS — bukan pola mobilitas kota yang sebenarnya.")
    hm = baca("ojol_h3.gpkg", "h3")
    kolom = st.radio("Waktu", ["jemput_pagi", "antar_sore"], horizontal=True)
    peta(hm, kolom, "jemput_pagi", zoom=11)
    lalin = baca_csv("lalin_sintetis.csv")
    st.line_chart(lalin.groupby("jam")["kecepatan_kmj"].median(), y_label="median km/jam")
