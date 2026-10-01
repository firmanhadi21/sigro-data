"""Unduh dan bekukan data OpenStreetMap untuk kota di city_config.json.

Hasil (data/raw/<slug>/):
  osm_<slug>.gpkg  layer: batas_kota, kecamatan, kelurahan, bangunan, poi
  jalan_drive.graphml, jalan_walk.graphml
  snapshot.json    waktu unduh dan jumlah fitur (angka di video berasal dari snapshot ini)

Pemakaian: python scripts/fetch_osm.py config/semarang.json [--unduh-ulang]
Snapshot yang sudah ada tidak ditimpa, kecuali dengan --unduh-ulang.
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import geopandas as gpd
import osmnx as ox
import pandas as pd

ox.settings.use_cache = True
ox.settings.cache_folder = "data/cache/osmnx"
ox.settings.requests_timeout = 300
ox.settings.log_console = True  # tampilkan progres dan jeda antrean Overpass

POI_TAGS = {
    "amenity": ["school", "clinic", "hospital", "doctors", "marketplace", "place_of_worship", "university"],
    "healthcare": ["centre", "clinic", "hospital"],
    "shop": ["supermarket", "convenience"],
}


MIRROR = ["https://overpass-api.de/api",
          "https://maps.mail.ru/osm/tools/overpass/api"]


def tahan(fn, *args, **kw):
    """Coba server Overpass utama lalu mirror, dengan jeda yang makin panjang (server bersama bisa sibuk/menolak)."""
    for i in range(2 * len(MIRROR)):
        ox.settings.overpass_url = MIRROR[i % len(MIRROR)]
        # cek antrean (/api/status) hanya di server utama; format status mirror berbeda dan membuat osmnx menunggu terus
        ox.settings.overpass_rate_limit = i % len(MIRROR) == 0
        try:
            return fn(*args, **kw)
        except Exception as e:  # noqa: BLE001 — jaringan, 429, 504, dll.
            if type(e).__name__ == "InsufficientResponseError":
                raise  # kueri valid tetapi hasilnya kosong: jangan diulang
            jeda = 15 * (i + 1)
            print(f"  {ox.settings.overpass_url.split('/')[2]}: {type(e).__name__}; coba lagi dalam {jeda} dtk",
                  flush=True)
            time.sleep(jeda)
    raise RuntimeError("Semua server Overpass gagal; coba lagi nanti")


def keep_polygons(gdf):
    gdf = gdf[gdf.geometry.geom_type.isin(["Polygon", "MultiPolygon"])].copy()
    return gdf.reset_index()


def admin(poly, level):
    gdf = tahan(ox.features_from_polygon, poly, {"boundary": "administrative", "admin_level": str(level)})
    gdf = keep_polygons(gdf)
    # batas wilayah adalah relasi; way tertutup bertag boundary biasanya gedung kantor kecamatan/kelurahan
    gdf = gdf[(gdf["element"] == "relation") & (gdf["admin_level"] == str(level))]
    # hanya unit yang pusatnya di dalam kota (tetangga di tepi ikut terunduh)
    inside = gdf.representative_point().within(poly)
    return gdf.loc[inside, ["id", "name", "admin_level", "geometry"]].reset_index(drop=True)


def main(cfg_path, unduh_ulang=False):
    cfg = json.loads(Path(cfg_path).read_text())
    out = Path("data/raw") / cfg["slug"]
    out.mkdir(parents=True, exist_ok=True)
    gpkg = out / f"osm_{cfg['slug']}.gpkg"
    if (out / "snapshot.json").exists() and not unduh_ulang:
        snap = json.loads((out / "snapshot.json").read_text())
        print(f"snapshot {cfg['name']} sudah ada ({snap['downloaded_utc']}); tidak diunduh ulang. "
              "Tambahkan --unduh-ulang untuk data OSM terbaru (angka akan berbeda dari video).")
        return
    t0 = time.time()

    kota = tahan(ox.geocode_to_gdf, cfg["osm_query"])[["display_name", "geometry"]]
    poly = kota.geometry.iloc[0]
    kota.to_file(gpkg, layer="batas_kota")

    kec = admin(poly, 6).rename(columns={"name": "kecamatan"})
    kel = admin(poly, 7).rename(columns={"name": "kelurahan"})
    # nama kelurahan tidak unik di satu kota (Semarang punya dua Purwosari): simpan kecamatannya,
    # dan gunakan kolom id (OSM relation id) sebagai kunci join
    pt = kel.set_geometry(kel.representative_point())
    kel["kecamatan"] = gpd.sjoin(pt, kec[["kecamatan", "geometry"]], predicate="within", how="left")["kecamatan"]
    kec.to_file(gpkg, layer="kecamatan")
    kel[["id", "kelurahan", "kecamatan", "admin_level", "geometry"]].to_file(gpkg, layer="kelurahan")

    bld = tahan(ox.features_from_polygon, poly, {"building": True})
    bld = keep_polygons(bld)
    cols = [c for c in ["id", "building", "building:levels", "height", "name", "geometry"] if c in bld]
    bld[cols].to_file(gpkg, layer="bangunan")

    poi = tahan(ox.features_from_polygon, poly, POI_TAGS).reset_index()
    poi["geometry"] = poi.geometry.representative_point()
    cols = [c for c in ["element", "id", "name", "amenity", "healthcare", "shop", "geometry"] if c in poi]
    poi[cols].to_file(gpkg, layer="poi")

    counts = {}
    for net in ["drive", "walk"]:
        g = tahan(ox.graph_from_polygon, poly, network_type=net)
        ox.save_graphml(g, out / f"jalan_{net}.graphml")
        counts[f"jalan_{net}"] = {"nodes": g.number_of_nodes(), "edges": g.number_of_edges()}

    for layer in ["kecamatan", "kelurahan", "bangunan", "poi"]:
        counts[layer] = len(gpd.read_file(gpkg, layer=layer))
    snap = {"city": cfg["name"], "downloaded_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "osmnx": ox.__version__, "counts": counts, "seconds": round(time.time() - t0)}
    (out / "snapshot.json").write_text(json.dumps(snap, indent=2))
    print(json.dumps(snap, indent=2))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main(args[0] if args else "city_config.json", unduh_ulang="--unduh-ulang" in sys.argv)
