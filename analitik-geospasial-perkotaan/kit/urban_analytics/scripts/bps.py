"""Membersihkan tabel ekspor BPS (CSV dari halaman tabel statistik bps.go.id).

Ekspor BPS diformat untuk dibaca manusia: BOM di awal berkas, beberapa baris judul, header bertingkat,
baris total di bawah, dan label yang tidak seragam antar-kota/tahun. Fungsi di sini mengubahnya menjadi tabel
rapi — berkas mentah tidak pernah diubah.
"""
import re
import unicodedata

import pandas as pd


def kunci_nama(s):
    """Kunci pencocokan nama wilayah: huruf kecil, tanpa spasi/tanda hubung/tanda baca."""
    s = unicodedata.normalize("NFKD", str(s)).lower()
    return re.sub(r"[^a-z0-9]", "", s)


def _kolom(label):
    k = kunci_nama(label)
    if k.startswith("laki"):
        return "laki_laki"
    if k.startswith("perempuan"):
        return "perempuan"
    if k in ("jumlah", "total"):
        return "jumlah"
    return k


def baca_penduduk_bps(path):
    """Tabel 'Jumlah Penduduk Menurut Kecamatan dan Jenis Kelamin' → DataFrame rapi + laporan pemeriksaan."""
    raw = pd.read_csv(path, header=None, encoding="utf-8-sig", dtype=str)  # utf-8-sig membuang BOM
    # baris header: dari baris pertama sampai baris yang memuat tahun (4 digit) di kolom data
    def baris_tahun_p(r):
        v = r.iloc[1:].dropna()
        return len(v) > 0 and v.str.fullmatch(r"\d{4}").all()  # baris kosong bukan baris tahun

    baris_tahun = next(i for i, r in raw.iterrows() if baris_tahun_p(r))
    label = raw.iloc[baris_tahun - 1, 1:].map(_kolom).tolist()
    tahun = int(raw.iloc[baris_tahun, 1])
    data = raw.iloc[baris_tahun + 1:].copy()
    data.columns = ["kecamatan"] + label
    data["kecamatan"] = data["kecamatan"].str.strip()

    total_mask = data["kecamatan"].map(kunci_nama).str.match(r"^(jumlah|total|kota)")
    total = data[total_mask]
    data = data[~total_mask].copy()
    for c in label:
        data[c] = pd.to_numeric(data[c].str.replace(r"[.\s]", "", regex=True))
    if "jumlah" not in data:
        data["jumlah"] = data["laki_laki"] + data["perempuan"]
    data["tahun"] = tahun

    cek = {"tahun": tahun, "baris_header": baris_tahun + 1, "kecamatan": len(data),
           "baris_total_dibuang": len(total)}
    if len(total):
        t = pd.to_numeric(total.iloc[0][label].str.replace(r"[.\s]", "", regex=True))
        cek["total_bps"] = int(t.get("jumlah", t.get("laki_laki", 0) + t.get("perempuan", 0)))
        cek["total_hitung"] = int(data["jumlah"].sum())
        cek["total_cocok"] = cek["total_bps"] == cek["total_hitung"]
    return data.reset_index(drop=True), cek
