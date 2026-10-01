# Analisis Kesesuaian Lokasi dan Aksesibilitas dengan QGIS — data latihan

Kursus gratis di sigro.id (Firman Hadi). Kasus: keluarga muda dengan anak kecil mencari tempat tinggal di kode pos
11201, Brooklyn, New York (mengikuti Belajar SIG, Bab 7.4 "Analisis kesesuaian").

## Unduhan (rilis `analisis-kesesuaian-aksesibilitas-v1`)

[`kesesuaian-brooklyn-latihan.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/analisis-kesesuaian-aksesibilitas-v1/kesesuaian-brooklyn-latihan.zip) (2 MB).

| Folder | Isi |
|---|---|
| `vector/` | 13 shapefile: `zipcode_bound` (area studi), `hurricane_evacuation_zones`, `hurricane_inundation_zones`, `noise` (12.472 keluhan kebisingan), `subway_entrances`, `elementary_schools`, `parks`, `bike_routes`, `athletic_facilities`, `museumart`, `residential_zoning`, `building_footprints`, `brooklyn_borough` |
| `raster/` | `grid_10kaki.tif` (grid analisis 951 × 826 sel, 10 kaki), `noise_heatmap_clip.tif`, `tree_density.tif`, `museumart_density.tif` |
| `hasil/` | kosong: simpan keluaran di sini |

**Sistem koordinat:** EPSG:2263 — NAD83 / New York Long Island (ftUS). Satuan **kaki** (US survey foot); 1 m = 3,28 kaki.
Di setiap dialog Rasterize: *Output extent › Calculate from Layer › grid_10kaki*, resolusi 10 × 10.

Dibanding paket asli Day6 (Belajar SIG): kolom jawaban `rank` dihapus dari `hurricane_evacuation_zones`, dan `noise`
dipangkas ke area studi + 5.000 kaki dengan tiga kolom (ukuran asli 264 MB). Tiga raster kepadatan diambil apa adanya
dari data buku sumber.

## Sumber dan lisensi

- Data asli dari **NYC Open Data** (City of New York), lihat ketentuan penggunaan di opendata.cityofnewyork.us.
- Paket Day6, Belajar SIG (Firman Hadi): https://firmanhadi.github.io/training-for-gis-analyses/img/Day6.zip
