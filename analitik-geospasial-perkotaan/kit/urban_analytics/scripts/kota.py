"""Utilitas bersama: konfigurasi kota dan lokasi folder.

Setiap notebook memulai dengan:
    from kota import CFG, RAW, PROC, OUT
Kota aktif ditentukan oleh city_config.json di akar proyek (salin dari config/<kota>.json),
atau oleh variabel lingkungan KOTA_CONFIG.
"""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_config(path=None):
    path = Path(path or os.environ.get("KOTA_CONFIG") or ROOT / "city_config.json")
    if not path.is_absolute():
        path = ROOT / path
    return json.loads(path.read_text())


CFG = load_config()
RAW = ROOT / "data" / "raw" / CFG["slug"]
PROC = ROOT / "data" / "processed" / CFG["slug"]
OUT = ROOT / "output" / CFG["slug"]
for _p in (RAW, PROC, OUT):
    _p.mkdir(parents=True, exist_ok=True)

OSM = RAW / f"osm_{CFG['slug']}.gpkg"
UTM = f"EPSG:{CFG['epsg_utm']}"
