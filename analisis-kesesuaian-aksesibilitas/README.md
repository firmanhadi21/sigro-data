# Analisis Kesesuaian Lokasi dan Aksesibilitas dengan QGIS — data latihan

Kursus gratis di sigro.id (Firman Hadi). Kasus: keluarga muda dengan anak kecil mencari tempat tinggal di kode pos
11201, Brooklyn, New York (mengikuti Belajar SIG, Bab 7.4 "Analisis kesesuaian").

## Unduhan (rilis `analisis-kesesuaian-aksesibilitas-v1`)

[`kesesuaian-day6-suitability.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/analisis-kesesuaian-aksesibilitas-v1/kesesuaian-day6-suitability.zip) (17 MB; 302 MB setelah diekstrak).

Isinya folder `Day6/SHP/suitability_analysis` dari paket Day6 Belajar SIG, dengan jalur yang sama, sehingga langkah di
video ("data kursus ada di `Day6/SHP/suitability_analysis`") tetap berlaku. Paket Day6 asli juga masih tersedia di
https://firmanhadi.github.io/training-for-gis-analyses/img/Day6.zip (40 MB); folder `Laos` dan `TIF`-nya tidak dipakai
kursus ini dan tidak disertakan di sini.

| Folder | Isi |
|---|---|
| `vector/` | `zipcode_bound` (area studi), `hurricane_evacuation_zones`, `hurricane_inundation_zones`, `noise`, `subway_entrances`, `elementary_schools`, `parks`, `bike_routes`, `athletic_facilities`, `museumart`, `residential_zoning`, `building_footprints`, `brooklyn_borough`, `ny_boroughs`, `max_suitability_polygons` |
| `raster/` | raster masukan (`noise_heatmap_clip`, `tree_density`, `museumart_density`) dan raster hasil tahap demi tahap dari buku sumber (`*_proximity`, `*_ranks`, `suitability`, `max_suitability`) untuk pembanding |
| `07_suitability_analysis.qgs` | proyek QGIS dari buku sumber |

**Sistem koordinat:** EPSG:2263 — NAD83 / New York Long Island (ftUS). Satuan **kaki** (US survey foot); 1 m = 3,28 kaki.

## Sumber dan lisensi

- Data asli dari **NYC Open Data** (City of New York); lihat ketentuan penggunaan di opendata.cityofnewyork.us.
- Paket Day6, Belajar SIG (Firman Hadi): https://firmanhadi.github.io/belajar-sig/hari_keenam.html#analisis-kesesuaian
