# RustGIS Tutorial — paket latihan

Kursus: https://sigro.id/course/rustgis-tutorial · Perangkat: [RustGIS](https://github.com/opengeos/RustGIS)
**0.3.0** (Apache-2.0)

Unduh: [`rustgis-tutorial.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/rustgis-tutorial-v1/rustgis-tutorial.zip)
(45 MB). Ekstrak; Anda mendapat folder `rustgis-tutorial/` — simpan di folder pengguna Anda
(Windows `C:\Users\<nama>\rustgis-tutorial`, macOS/Linux `~/rustgis-tutorial`). Video kursus menunjuk berkas dengan jalur
di bawah ini. Wilayah latihan: **Semarang Raya** (110,22–110,55 BT; 7,22–6,88 LS).

| Berkas | Isi | Pelajaran |
|---|---|---|
| `data/geojson/*.geojson` | kabupaten, kecamatan, desa; jalan, sungai, permukiman, sekolah, fasilitas kesehatan, tempat ibadah | hampir semua |
| `data/geojson/sekolah_per_kecamatan.geojson` | jumlah sekolah per kecamatan (kolom `point_count`) | p31, p32, p91, p92 |
| `data/geojson/usulan_posyandu.geojson` | satu titik contoh **FIKTIF** (kolom `nama`, `status`) untuk berlatih menyunting | p41 |
| `data/shp/kecamatan.shp`, `data/shp/kecamatan_utm.shp` | kecamatan sebagai Shapefile, lintang-bujur dan UTM 49S | p21 |
| `data/sekolah.csv` | sekolah dengan kolom `lon`, `lat` | p21 |
| `data/semarang.gpkg` | semua lapisan vektor dalam satu GeoPackage | p02, p21 |
| `data/semarang_s2.tif` | komposit median Sentinel-2 L2A Juni–Oktober 2024, 20 m; band biru, hijau, merah, NIR, SWIR | p61, p62 |
| `data/semarang_dem.tif` | elevasi Copernicus GLO-30 | p21, p71, p72, p81 |
| `data/semarang_worldcover.tif` | tutupan lahan ESA WorldCover 2021 | p81 |
| `data/semarang_worldpop.tif` | sebaran penduduk WorldPop | latihan mandiri |
| `perintah/p72.txt`, `perintah/p81.txt` | perintah siap salin untuk panel Script | p72, p81 |
| `perintah/p101.sh` | alur kerja buffer–erase dengan `rustgis-cli` | p101 |
| `perintah/p121.txt`, `perintah/p122.txt` | OpenStreetMap, Overture, geoBoundaries, dan pencarian STAC sebagai perintah panel Script | p121, p122 |
| `perintah/p123.txt` | alamat layanan peta BIG untuk Add Data › From Service | p123 |
| `perintah/p131.sql` | dua kueri untuk panel SQL (perlu [DuckDB](https://duckdb.org/install/)) | p131 |
| `notebooks/p132_python.ipynb` | analisis modul R5 dari Python (`pip install "rustgis[jupyter]==0.3.0" geopandas jupyterlab`) | p132 |

Semua data dalam EPSG:4326, kecuali `kecamatan_utm.shp`.

## Lisensi

- Batas wilayah: Indonesia COD-AB (BPS), via [HDX](https://data.humdata.org), CC BY-IGO.
- Jalan, sungai, permukiman, sekolah, fasilitas kesehatan, tempat ibadah: © kontributor OpenStreetMap,
  [ODbL 1.0](https://www.openstreetmap.org/copyright). Sebut sumbernya setiap kali dipakai.
- Sentinel-2 L2A: Copernicus Sentinel data 2024 (diolah lewat Google Earth Engine).
- Copernicus DEM GLO-30: © DLR e.V. 2010–2014 dan © Airbus Defence and Space GmbH 2014–2018, program Copernicus.
- ESA WorldCover 2021: © ESA WorldCover project / Contains modified Copernicus Sentinel data (2021), CC BY 4.0.
- WorldPop (www.worldpop.org), CC BY 4.0.
- `sekolah_per_kecamatan` dan `usulan_posyandu` (fiktif): dibuat untuk kursus ini dari data di atas (CC BY 4.0, sigro.id).
