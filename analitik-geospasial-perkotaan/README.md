# Analitik Geospasial Perkotaan — paket data dan paket latihan

Kursus eksklusif di sigro.id (Firman Hadi): pipeline analitik perkotaan dari data terbuka sampai dasbor, untuk Kota
Semarang dan Kota Makassar.

## Unduhan (rilis `analitik-geospasial-perkotaan-v1`)

| Berkas | Isi |
|---|---|
| [`analitik-perkotaan-kit.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/analitik-geospasial-perkotaan-v1/analitik-perkotaan-kit.zip) (0,1 MB) | Paket latihan: notebook, skrip, konfigurasi kota, dasbor — sama dengan folder [`kit/`](kit/) |
| [`analitik-perkotaan-data.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/analitik-geospasial-perkotaan-v1/analitik-perkotaan-data.zip) (91 MB) | Snapshot data: ekstrak ke folder `urban_analytics/` sehingga isinya masuk ke `data/raw/` |

Data dibekukan agar angka Anda sama dengan angka di video. OpenStreetMap berubah setiap hari; skrip
`scripts/fetch_osm.py --unduh-ulang` di paket latihan mengambil data terbaru (angkanya akan berbeda).

## Isi paket data (per kota)

| Berkas | Isi |
|---|---|
| `snapshot.json` | Waktu unduh dan jumlah fitur |
| `osm_<kota>.gpkg` | Batas kota, kecamatan, kelurahan, bangunan, POI (OpenStreetMap) |
| `jalan_drive.graphml`, `jalan_walk.graphml` | Jaringan jalan kendaraan dan pejalan kaki (OSMnx) |
| `ghlc/ghlc30_2020…2024.tif`, `ghlc/ghlc10_2020.tif` | Jendela Global Harmonized Land Cover, UTM |

| Kota | Diunduh (UTC) | Kelurahan | Bangunan |
|---|---|---|---|
| Semarang | 2026-09-29 12:21 | 177 | 521.622 |
| Makassar | 2026-09-29 14:42 | 153 | 252.408 |

## Sumber dan lisensi

- **OpenStreetMap** — © kontributor OpenStreetMap, [ODbL 1.0](https://opendatacommons.org/licenses/odbl/).
  Berkas `osm_*.gpkg` dan `jalan_*.graphml` adalah basis data turunan dan tetap berlisensi ODbL.
- **Global Harmonized Land Cover (GHLC)** — OpenGeoHub / LandMetric; Moreno et al. (2026),
  https://doi.org/10.5194/egusphere-2026-5540; data asli: https://source.coop/opengeohub/ogh-ghlc10
  (lihat lisensi di halaman sumber).
- **Tabel penduduk BPS** di `data/raw/<kota>/bps_penduduk_kecamatan.csv` — Badan Pusat Statistik.
- Zonasi, lalu lintas, dan data ojol yang dibuat di dalam notebook adalah **data sintetis** untuk latihan.

## Earth Engine

Notebook 10 dan 11 memakai Google Earth Engine dengan akun Anda sendiri (`earthengine authenticate`, lalu isi
`EE_PROJECT`). Paket ini tidak berisi kredensial apa pun; jangan pernah meng-commit berkas kunci.
