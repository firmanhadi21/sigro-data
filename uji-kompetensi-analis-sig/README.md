# Persiapan Uji Kompetensi Analis SIG (Jenjang 6) — data latihan

Kursus eksklusif di sigro.id (Firman Hadi): persiapan uji kompetensi skema Analis SIG berdasarkan SKKNI Informasi
Geospasial 2020, dikerjakan di QGIS 4.2 dan PostGIS dengan data Kota Semarang.

## Unduhan (rilis `uji-kompetensi-analis-sig-v1`)

[`ukom-analis-sig-data.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/uji-kompetensi-analis-sig-v1/ukom-analis-sig-data.zip) (35 MB).
Ekstrak sehingga Anda punya folder `ukom/` berisi `data/` dan `sql/`.

| Berkas | Isi | Pelajaran |
|---|---|---|
| `data/ukom_semarang.gpkg` | batas_kota, kecamatan (16), kelurahan (177), lembar, bangunan_lembar, jalan, sungai, rel, tutupan, perairan, poi (5.737), kontur, titik_tinggi — EPSG:32749 | hampir semua |
| `data/ukom_qc.gpkg` | `kelurahan_qc`: batas kelurahan dengan cacat yang disengaja | 7.2 |
| `data/dem_semarang.tif` | DEM 30 m, EPSG:32749 (tanpa NoData — lihat pelajaran 4.3) | 4.2, 4.3, 6.3, 6.5 |
| `data/worldpop_semarang.tif` | penduduk per sel 100 m, EPSG:32749 | 6.2, 6.4, 6.5, 8.1 |
| `data/titik_ukur.csv` | titik pengukuran (kolom x, y dalam EPSG:32749) | 4.2 |
| `sql/layanan_ddl.sql`, `sql/layanan_jenis.sql` | model fisik dan tabel acuan skema `layanan` — juga di folder [`sql/`](sql/) | 2.3 |
| `sql/layanan_isi.sql` | mengisi skema `layanan` dari skema `sumber` | 2.4 |

Perangkat lunak: QGIS 4.2, PostgreSQL 17 dengan PostGIS 3.5 (modul 2, 3, dan 8).

**Peta cetak:** pelajaran 1.4–1.5 memakai Peta Rupabumi Indonesia 1:25.000 Lembar 1409-222 SEMARANG (Edisi I-2001).
Pindaian lembar itu dilindungi hak cipta dan **tidak** disertakan; dapatkan dari Badan Informasi Geospasial.

## Sumber dan lisensi

- **OpenStreetMap** — © kontributor OpenStreetMap, ODbL 1.0 (snapshot 29 September 2026). Layer turunannya tetap ODbL.
- **DEM** — Copernicus GLO-30 © DLR e.V. 2010–2014 dan © Airbus Defence and Space GmbH 2014–2018, disediakan di bawah
  program COPERNICUS oleh Uni Eropa dan ESA.
- **Penduduk** — WorldPop (www.worldpop.org), CC BY 4.0.
- Cacat pada `ukom_qc.gpkg` dan titik pada `titik_ukur.csv` dibuat untuk latihan.
