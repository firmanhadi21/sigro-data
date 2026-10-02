# Analisis Data Sosial dengan R — paket latihan

Kursus gratis di sigro.id (Firman Hadi): R, RStudio, dan Quarto untuk pemula ilmu sosial, dengan data Indonesia.

## Unduhan (rilis `analisis-data-sosial-r-v1`)

[`analisis-data-sosial-r-kit.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/analisis-data-sosial-r-v1/analisis-data-sosial-r-kit.zip) (3,5 MB).
Ekstrak, lalu buka `sosial/sosial.Rproj` di RStudio.

| Berkas | Isi |
|---|---|
| `p03-mulai.qmd` … `p102-laporan.qmd` | Satu dokumen Quarto per praktik, potongan kode masih kosong (diisi sambil mengikuti video) |
| `data/kabupaten_2018.csv` | 514 kabupaten dan kota × 35 kolom, kunci `kode` (kode wilayah Kemendagri, baca sebagai teks): penduduk, kemiskinan, IPM, PDRB, desa beraspal, listrik, melek huruf, dokter, SD, penganggur, pengeluaran per kapita (2018, sebagian 2014); luas dan kepadatan; cahaya malam 2014 dan 2018; Pilpres 2024 (suara, persen, cakupan TPS) |
| `data/kabupaten.gpkg` | Batas 514 kabupaten dan kota, disederhanakan, EPSG:4326 |
| `data/proyek_jalan_desa.csv` | 567 proyek jalan desa dari eksperimen audit Olken (2007) |

**Galat yang diketahui, sengaja dibiarkan** (ditemukan peserta di pelajaran 5.3): PDRB 2018 Malaka, Sabu Raijua, dan
Malinau kurang dari Rp 1 juta per orang; PDRB 2014 Takalar dan Sorong terlalu besar.

## Sumber dan lisensi

- **INDO-DAPOER** (Indonesia Database for Policy and Economic Research), Bank Dunia, dari data BPS — CC BY 4.0.
- **Cahaya malam** — VIIRS Nighttime Lights V2.1 tahunan, Earth Observation Group, Payne Institute for Public Policy,
  Colorado School of Mines — CC BY 4.0. Dijumlahkan per kabupaten.
- **Batas wilayah** — geoBoundaries (Runfola dkk. 2020), IDN ADM2 — CC BY 3.0 IGO. Disederhanakan.
- **Pilpres 2024** — KawalPemilu.org (Ainun Najib dan relawan), rekap formulir C1 per TPS, dijumlahkan per kabupaten.
- **Eksperimen audit** — Olken, B. A. (2007). Monitoring Corruption: Evidence from a Field Experiment in Indonesia.
  *Journal of Political Economy* 115(2). Data replikasi: Harvard Dataverse hdl:1902.1/10366 — CC0.
