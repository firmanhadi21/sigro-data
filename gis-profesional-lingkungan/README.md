# GIS untuk Profesional Lingkungan — data latihan

Kursus: https://sigro.id/course/gis-profesional-lingkungan

Unduh: [`gis-profesional-lingkungan-data.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/gis-profesional-lingkungan-v1/gis-profesional-lingkungan-data.zip) (60 MB). Ekstrak; Anda mendapat folder `lingkungan/` berisi `data/` dan `LISENSI.md`.

Studi kasus: hutan rawa gambut Sebangau dan Kota Palangka Raya, Kalimantan Tengah. CRS: WGS 84 / UTM zona 49S (EPSG:32749), kecuali CSV (WGS 84, EPSG:4326).

| Berkas | Isi | Pelajaran |
|---|---|---|
| `lingkungan_sebangau.gpkg` | taman_nasional (bagian TN Sebangau di area latihan), sungai, kanal, jalan, permukiman (OSM); desa (HDX COD-AB/BPS) | semua |
| `sebangau_s2.tif` | Sentinel-2 L2A, median musim kemarau 2024; band 1 B2, 2 B3, 3 B4, 4 B8, 5 B11 (20 m) | A0, A1, A3, A5 |
| `sebangau_dem.tif` | Copernicus DEM GLO-30 | A3b |
| `sebangau_worldcover.tif` | ESA WorldCover 2021 (20 m) | A4a, A6b |
| `sebangau_hansen_treecover2000.tif`, `sebangau_hansen_lossyear.tif` | Hansen/UMD Global Forest Change v1.12 (30 m) | A6 |
| `burung_gbif_sebangau.csv` | 1.447 pengamatan burung GBIF (hanya rekaman CC0 dan CC BY), kolom `lon`, `lat`, `iucn`, `lisensi` | A1b, A4b, A5 |
| `burung_iucn_okabe.qml` | gaya kategori IUCN, palet Okabe–Ito | A5 |

## Lisensi

OpenStreetMap (ODbL 1.0) · HDX COD-AB/BPS (CC BY-IGO) · Copernicus Sentinel dan Copernicus DEM (lisensi Copernicus,
dengan atribusi) · ESA WorldCover, Hansen GFC (CC BY 4.0) · GBIF.org (per rekaman: CC0 atau CC BY). Rincian di `LISENSI.md`.
