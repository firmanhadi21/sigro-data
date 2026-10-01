"""Buat tabel sederhana (CSV) dari snapshot OSM untuk latihan pandas di notebook 01.

Hasil (data/raw/<kota>/): kecamatan.csv (kecamatan, luas_km2), kelurahan.csv (kelurahan, kecamatan, luas_ha,
n_bangunan). Pemakaian: python scripts/buat_tabel.py
"""
import sys
from pathlib import Path

import geopandas as gpd

sys.path.insert(0, str(Path(__file__).parent))
from kota import OSM, RAW, UTM  # noqa: E402

kec = gpd.read_file(OSM, layer="kecamatan").to_crs(UTM)
kel = gpd.read_file(OSM, layer="kelurahan").to_crs(UTM)
bld = gpd.read_file(OSM, layer="bangunan", columns=["id"]).to_crs(UTM)

kec["luas_km2"] = (kec.area / 1e6).round(2)
kec[["kecamatan", "luas_km2"]].sort_values("kecamatan").to_csv(RAW / "kecamatan.csv", index=False)

kel["luas_ha"] = (kel.area / 1e4).round(1)
j = gpd.sjoin(bld.set_geometry(bld.representative_point()), kel[["id", "geometry"]].rename(columns={"id": "kid"}),
              predicate="within")
kel["n_bangunan"] = kel["id"].map(j.groupby("kid").size()).fillna(0).astype(int)
kel[["kelurahan", "kecamatan", "luas_ha", "n_bangunan"]].sort_values(["kecamatan", "kelurahan"]) \
    .to_csv(RAW / "kelurahan.csv", index=False)
print("tersimpan: kecamatan.csv", len(kec), "baris; kelurahan.csv", len(kel), "baris")
