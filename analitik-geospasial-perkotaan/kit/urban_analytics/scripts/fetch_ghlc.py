"""Potong Global Harmonized Land Cover (GHLC, OpenGeoHub) untuk kota aktif, langsung dari COG di internet.

GHLC 30 m tahunan 2020–2024 dan 10 m untuk 2020 (Moreno et al., 2026; https://source.coop/opengeohub/ogh-ghlc10).
Berkas global berukuran puluhan GB, tetapi format COG memungkinkan GDAL membaca hanya jendela kota kita.
Hasil: data/raw/<kota>/ghlc/ghlc30_<tahun>.tif dan ghlc10_2020.tif (UTM, tetangga terdekat).

Pemakaian: python scripts/fetch_ghlc.py
"""
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from kota import CFG, RAW, UTM  # noqa: E402

URL = ("/vsicurl/https://data.source.coop/opengeohub/ogh-ghlc10/"
       "land.cover_ifad.mcdt_c_{res}m_s_{y}0101_{y}1231_go_epsg.4326_v1.2.tif")
env = dict(os.environ, GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR")

out = RAW / "ghlc"
out.mkdir(exist_ok=True)
w, s, e, n = CFG["bbox"]
for res, y in [(30, y) for y in range(2020, 2025)] + [(10, 2020)]:
    f = out / f"ghlc{res}_{y}.tif"
    if f.exists():
        continue
    subprocess.run(["gdalwarp", "-q", "-te", str(w), str(s), str(e), str(n), "-te_srs", "EPSG:4326",
                    "-t_srs", UTM, "-tr", str(res), str(res), "-r", "near", "-co", "COMPRESS=DEFLATE",
                    URL.format(res=res, y=y), str(f)], check=True, env=env)
    print("tersimpan", f.name)
