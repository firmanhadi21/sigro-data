"""Jalankan seluruh pipeline untuk satu kota: unduh data, lalu eksekusi semua notebook berurutan.

Pemakaian:  python scripts/jalankan_pipeline.py config/makassar.json [--unduh-ulang]
Snapshot OSM yang sudah ada dipakai ulang (angka tetap sama); --unduh-ulang mengambil data OSM terbaru.
Notebook yang gagal dicatat, lalu pipeline berlanjut ke notebook yang tidak bergantung padanya.
Notebook hasil eksekusi disimpan di output/<kota>/notebooks/; periksa hasilnya dengan scripts/laporan.py.
Notebook 09 butuh DATABASE_URL; 10–11 butuh kredensial Earth Engine (EE_KEY atau EE_PROJECT).
"""
import contextlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import papermill as pm

@contextlib.contextmanager
def diam():
    """Hide the kernel's stderr (connection and GDAL warnings); errors still end up in status.json and the notebook."""
    simpan, nul = os.dup(2), os.open(os.devnull, os.O_WRONLY)
    os.dup2(nul, 2)
    try:
        yield
    finally:
        os.dup2(simpan, 2)
        os.close(nul)
        os.close(simpan)


ROOT = Path(__file__).resolve().parents[1]
argv = [a for a in sys.argv[1:] if not a.startswith("--")]
UNDUH_ULANG = "--unduh-ulang" in sys.argv
cfg_path = Path(argv[0] if argv else "city_config.json")
cfg = json.loads((ROOT / cfg_path).read_text())
env = dict(os.environ, KOTA_CONFIG=str(cfg_path))
os.environ.update(env)

LANGKAH = ["fetch_osm.py", "fetch_ghlc.py", "buat_tabel.py"]
NOTEBOOK = {  # notebook: notebook lain yang harus berhasil lebih dulu
    "00_persiapan": [], "01_python_dasar": [], "02_akuisisi_data": [], "03_membersihkan_bps": [],
    "04_morfologi": [],
    "05_kdb_klb": ["04_morfologi"], "06_h3": ["04_morfologi"], "07_osmnx": [],
    "08_space_syntax": ["04_morfologi", "07_osmnx"], "09_postgis": ["05_kdb_klb", "07_osmnx"],
    "10_gee_perubahan_lahan": ["04_morfologi"], "11_gee_risiko_pesisir": ["04_morfologi"],
    "12_mobilitas_sintetis": ["04_morfologi", "08_space_syntax"],
}

print(f"== {cfg['name']} ({cfg_path})")
snap = ROOT / "data" / "raw" / cfg["slug"] / "snapshot.json"
for s in LANGKAH:
    if s == "fetch_osm.py" and snap.exists() and not UNDUH_ULANG:
        print(f"snapshot OSM ada ({json.loads(snap.read_text())['downloaded_utc']}), tidak diunduh ulang", flush=True)
        continue
    subprocess.run([sys.executable, str(ROOT / "scripts" / s), str(cfg_path)], check=True, cwd=ROOT, env=env)

out = ROOT / "output" / cfg["slug"] / "notebooks"
out.mkdir(parents=True, exist_ok=True)
status = {}
for nb, butuh in NOTEBOOK.items():
    gagal = [b for b in butuh if status.get(b) != "ok"]
    if gagal:
        status[nb] = f"dilewati (butuh {', '.join(gagal)})"
    elif nb == "09_postgis" and "DATABASE_URL" not in os.environ:
        status[nb] = "dilewati (DATABASE_URL tidak diisi)"
    else:
        t0 = time.time()
        try:
            with diam():
                pm.execute_notebook(ROOT / "notebooks" / f"{nb}.ipynb", out / f"{nb}.ipynb",
                                    cwd=str(ROOT / "notebooks"), kernel_name="python3", progress_bar=False)
            status[nb] = "ok"
        except pm.PapermillExecutionError as e:
            status[nb] = f"GAGAL di sel {e.exec_count}: {e.ename}: {str(e.evalue)[:120]}"
        print(f"{nb:26} {status[nb]}  ({time.time() - t0:.0f} dtk)", flush=True)
        continue
    print(f"{nb:26} {status[nb]}", flush=True)

(out / "status.json").write_text(json.dumps(status, indent=2, ensure_ascii=False))
print(f"\n{sum(v == 'ok' for v in status.values())}/{len(status)} notebook berhasil — lihat {out}/status.json")
