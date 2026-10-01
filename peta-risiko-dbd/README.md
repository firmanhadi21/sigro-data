# Peta Risiko Demam Berdarah Dengue dengan QGIS Processing Modeler — data latihan

Kursus gratis di sigro.id (Firman Hadi).

## Unduhan (rilis `peta-risiko-dbd-v1`)

[`dbd-semarang-latihan.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/peta-risiko-dbd-v1/dbd-semarang-latihan.zip) (3 MB).
Model dan skrip contohnya juga ada langsung di folder ini.

| Berkas | Isi |
|---|---|
| `dbd_semarang.gpkg` | EPSG:32749. `kelurahan` (177 poligon: kode_kel, kelurahan, kecamatan, luas_km2, penduduk), `kasus_dbd_2025` (950 titik), `puskesmas` (36), `stasiun_hujan` (16: ch_tahunan, hari_hujan) |
| `dem_semarang_30m.tif` | DEM 30 m, EPSG:32749 |
| [`model_risiko_dbd_semarang.model3`](model_risiko_dbd_semarang.model3) | Model Processing Modeler: 13 algoritma, 15 input, 5 output |
| [`jalankan_model.sh`](jalankan_model.sh) | Contoh menjalankan model dengan `qgis_process` |

**Penduduk, kasus DBD, Puskesmas, dan pos hujan adalah data SINTETIS untuk latihan.** Jangan digunakan sebagai
informasi epidemiologis nyata tentang Kota Semarang. Enam titik kasus sengaja berada di luar semua poligon kelurahan,
sehingga jumlah kasus per kelurahan 944, bukan 950 — bahan diskusi di kursus.

## Sumber dan lisensi

- **Batas kelurahan dan kecamatan** — © kontributor OpenStreetMap, ODbL 1.0; layer kelurahan adalah basis data turunan
  dan juga berlisensi ODbL.
- **DEM** — Copernicus GLO-30 © DLR e.V. 2010–2014 dan © Airbus Defence and Space GmbH 2014–2018, disediakan di bawah
  program COPERNICUS oleh Uni Eropa dan ESA.
- **Data sintetis** — dibuat oleh Firman Hadi untuk latihan.
