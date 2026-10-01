"""Laporan pemeriksaan setelah pipeline: status tiap notebook, lalu setiap baris keluaran yang berisi peringatan.

"Berhasil dijalankan" tidak sama dengan "benar". Notebook mencetak hasil pemeriksaan data (baris tanpa pasangan,
wilayah tanpa poligon, dll.); skrip ini mengumpulkannya dalam satu layar.
Pemakaian: python scripts/laporan.py makassar
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
slug = sys.argv[1] if len(sys.argv) > 1 else json.loads((ROOT / "city_config.json").read_text())["slug"]
nbdir = ROOT / "output" / slug / "notebooks"
status = json.loads((nbdir / "status.json").read_text())
ok = sum(v == "ok" for v in status.values())
print(f"{slug}: {ok}/{len(status)} notebook berhasil")
for nb, st in status.items():
    if st != "ok":
        print(f"  {nb}: {st}")

POLA = re.compile(r"tanpa |tidak |GAGAL|gagal|selisih|melampaui jelas", re.I)
print("\nperingatan dan pemeriksaan data:")
for f in sorted(nbdir.glob("*.ipynb")):
    for cell in json.loads(f.read_text())["cells"]:
        for o in cell.get("outputs", []):
            teks = "".join(o.get("text", [])) if o.get("output_type") == "stream" else ""
            for baris in teks.splitlines():
                if POLA.search(baris) and len(baris) < 140:
                    print(f"  {f.stem[:2]}  {baris.strip()}")
