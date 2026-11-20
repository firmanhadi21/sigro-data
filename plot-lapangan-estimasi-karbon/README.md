# Dari Plot Lapangan ke Estimasi Karbon — paket kursus

Kursus: https://sigro.id/course/plot-lapangan-estimasi-karbon

Unduh: [`plot-lapangan-estimasi-karbon-kit.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/plot-lapangan-estimasi-karbon-v1/plot-lapangan-estimasi-karbon-kit.zip)
(58 MB). Ekstrak; Anda mendapat folder `karbon-kit/`. Petunjuk lengkap ada di `karbon-kit/README.md`.

Lingkungan kerja dengan Docker: **PostGIS** yang sudah berisi data latihan, **RStudio** dengan semua paket R kursus
(image `ghcr.io/firmanhadi21/karbon-rstudio:0.1.0`, amd64 dan arm64: Windows, macOS Intel dan Apple silicon, Linux),
dan **mergin-db-sync** untuk menyambungkan survei Mergin Maps Anda sendiri.

```bash
cd karbon-kit
cp .env.example .env      # ganti POSTGRES_PASSWORD
docker compose up -d      # RStudio di http://localhost:8787
```

| Berkas / folder | Isi | Bagian |
|---|---|---|
| `mergin/survei-karbon/` | proyek Mergin Maps: formulir Survei pohon (protokol UNDIP: plot r 10 m, pohon DBH ≥ 10 cm), daftar 179 pohon kampus UNDIP + 18 mangrove | 2–3 |
| `initdb/` | data latihan + view pemeriksaan, dimuat otomatis ke PostGIS | 4 |
| `sql/qc.sql` | view pemeriksaan kualitas data (untuk skema survei Anda sendiri) | 4 |
| `05_biomassa.qmd` … `08_laporan.qmd`, `R/umum.R` | buku catatan R: biomassa, ketidakpastian, peta, laporan | 5–8 |
| `data/semarang/` | Sentinel-2 L2A median kemarau 2023, tinggi kanopi Meta/WRI, ESA WorldCover 2021 (10 m, Semarang) | 7 |
| `data/sintetis/` | survei latihan 80 plot (CSV, GeoPackage) dan batas wilayah kerja | 4–8 |
| `docker-compose.yml`, `.env.example`, `dbsync/` | lingkungan kerja | semua |

**Data latihan SINTETIS.** Lokasi plot diacak di Semarang dan pohonnya dibangkitkan dari pola data inventarisasi
sungguhan; beberapa kesalahan sengaja ditanam untuk latihan pemeriksaan data. Bukan angka karbon Semarang yang
sebenarnya. Kunci jawaban tidak ada di paket ini.

## Lisensi

- Sentinel-2 L2A: berisi data Copernicus Sentinel yang dimodifikasi (2023), diproses lewat Microsoft Planetary Computer.
- Tinggi kanopi global 1 m: Meta dan World Resources Institute (2024), CC BY 4.0.
- ESA WorldCover 10 m 2021 v200: © ESA WorldCover project / Copernicus Sentinel data (2021), CC BY 4.0.
- Daftar pohon Kampus Tembalang: Diponegoro Biodiversity Center, biodiversity.undip.ac.id.
- Data sintetis, formulir, SQL, dan buku catatan: dibuat untuk kursus ini (CC BY 4.0, sigro.id).
