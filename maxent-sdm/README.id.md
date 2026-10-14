# Pemodelan Sebaran Spesies dengan Maxent — kit kursus

[English](README.md) · Kursus: https://sigro.id/course/pemodelan-sebaran-spesies-maxent (versi bahasa Inggris:
https://sigro.id/course/maxent-sdm) · Perangkat lunak: [Maxent 3.4.4](https://github.com/mrmaxent/Maxent) (MIT),
[QGIS](https://qgis.org) 3.40 atau lebih baru, Java 11 atau lebih baru.

Unduhan: [`maxent-sdm.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/maxent-sdm-v1/maxent-sdm.zip) (87 MB) · [`maxent-sdm-java.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/maxent-sdm-v1/maxent-sdm-java.zip) (31 MB, untuk modul M10).

Ekstrak `maxent-sdm.zip` di folder pengguna Anda: Anda mendapat folder `maxent-course/` (Windows
`C:\Users\<nama>\maxent-course`, macOS/Linux `~/maxent-course`). Video memakai jalur yang persis sama. Untuk modul
M10, ekstrak `maxent-sdm-java.zip` di tempat yang sama: isinya menambahkan `maxent-course/layers_java/`.

Nama folder, berkas, dan kolom dalam kit memakai bahasa Inggris, sama untuk kedua versi kursus.

Wilayah kajian: **Banten dan Jawa Barat**. Semua grid: **UTM zona 48S (EPSG:32748), 100 m**, 4.165 × 2.261 sel,
ESRI ASCII (`.asc`), nodata −9999 (laut dan wilayah di luar wilayah kajian).

| Folder / berkas | Isi | Praktik |
|---|---|---|
| `layers/*.asc` | 14 grid lingkungan (tabel di bawah) | p31, p32, p51 – p91 |
| `layers_java/*.asc` | 10 lapisan yang dipakai model, untuk seluruh Pulau Jawa pada 250 m | p101 |
| `bias/bias_mammals.asc` | grid upaya pengambilan sampel kelompok target dari rekaman mamalia GBIF (1–100) | p82 |
| `gbif/hylobates_moloch_gbif.csv` | rekaman GBIF owa jawa, apa adanya seperti diunduh (174 baris, belum dibersihkan) | p21 |
| `occurrences/gbif_maxent.csv` | 6 lokalitas GBIF yang sudah bersih dalam format Maxent: `species,x,y` dalam UTM 48S | p51 dan seterusnya, latihan Anda |
| `boundaries/java.gpkg` | lapisan `java` (garis pantai) dan `study_area` (Banten + Jawa Barat), UTM 48S | p21, p22 |
| `sources/chelsa_bio12_rainfall.tif` | curah hujan tahunan CHELSA, 30 detik busur, bujur/lintang: masukan mentah `layers/rainfall.asc` | p31 |
| `scripts/correlation.py` | korelasi Pearson antarlapisan pada 10.000 sel daratan acak | p32 |
| `output/` | kosong: buat satu folder untuk setiap run Maxent atau QGIS di sini | semua |
| `glossary.md` | istilah yang dipakai dalam kursus (bahasa Inggris) | — |

## Lapisan

| Berkas | Variabel | Sumber, tahun | Catatan |
|---|---|---|---|
| `elevation` | elevasi, m | SRTM, 2000 | dibuang dari model (r = −0,99 dengan suhu) |
| `slope` | kemiringan lereng, derajat | dari SRTM | |
| `northness`, `eastness` | cos dan sin arah hadap lereng | dari SRTM | arah hadap bersifat sirkular |
| `dist_river`, `dist_road` | jarak ke sungai / jalan terdekat, m | OpenStreetMap (ekstrak Geofabrik, 2026-10-12) | jalan masa kini, bukan jalan pada tahun rekaman |
| `forest_function` | fungsi kawasan hutan, 5 kelas: 1 kawasan konservasi, 2 hutan lindung (HL), 3 hutan produksi (HP/HPT), 4 hutan produksi yang dapat dikonversi (HPK, tidak ada di sini), 5 areal penggunaan lain (APL) | KLHK, Penunjukan Kawasan Hutan 1:250.000 | **kategoris** di Maxent |
| `tree_height` | tinggi tajuk, m | ETH Global Canopy Height 2020 | |
| `tree_cover_2000` | tutupan pohon, % | Hansen Global Forest Change v1.13 | dibuang (r = 0,79 dengan tinggi pohon) |
| `ndvi` | median NDVI 2005–2009 | Landsat 5 dan 7 | dibuang (r = 0,78 dengan tinggi pohon) |
| `temperature` | suhu rata-rata tahunan, °C | CHELSA 2.1, 1981–2010 | |
| `rainfall` | curah hujan tahunan, mm | CHELSA 2.1, 1981–2010 | |
| `population` | jumlah penduduk per sel 100 m | WorldPop, 2005 | |
| `night_lights` | cahaya malam stabil, DN | DMSP-OLS, 2005 | dibuang (r = 0,80 dengan penduduk) |

## Tentang rekaman kehadiran

Video memodelkan **rekaman lapangan owa jawa** (Iskandar, Nursal, serta survei Sancang dan Priangan, 1992–2009).
Owa jawa terancam punah dan diburu untuk perdagangan satwa peliharaan, jadi **rekaman tersebut tidak ada di kit ini**,
begitu pula apa pun yang diturunkan darinya. Sebagai gantinya, kit ini berisi rekaman **GBIF** publik: praktik p21
membersihkannya, dan p22 mengubahnya menjadi `occurrences/gbif_maxent.csv`.

Enam lokalitas bersih terlalu sedikit untuk model yang andal — dengan kurang dari sepuluh rekaman Maxent hanya memakai
fitur linear — dan itu bagian dari pelajarannya: mutu rekaman lebih membatasi model daripada pengaturan apa pun.
Pakai rekaman ini untuk berlatih setiap langkah, bandingkan angka Anda dengan angka di video untuk melihat apa yang
berubah dengan rekaman yang lebih banyak dan lebih baik, dan tambahkan rekaman dari survei Anda sendiri bila bisa
(rahasiakan lokasi spesies terancam).

## Sumber dan lisensi

Sebutkan sumbernya setiap kali Anda memakai atau membagikan berkas-berkas ini.

| Berkas | Sumber | Lisensi |
|---|---|---|
| `layers/elevation`, `slope`, `northness`, `eastness`; versi Jawa | NASA SRTM (2000), via Google Earth Engine | domain publik |
| `layers/dist_river`, `dist_road` | © kontributor OpenStreetMap, ekstrak Geofabrik untuk Jawa (2026-10-12) | [ODbL 1.0](https://www.openstreetmap.org/copyright) — grid jarak adalah karya turunan (produced work): sebutkan OpenStreetMap |
| `layers/forest_function` | Kementerian Lingkungan Hidup dan Kehutanan (KLHK), *Penunjukan Kawasan Hutan* 1:250.000, dikelompokkan menjadi 5 kelas | data pemerintah, sumber KLHK |
| `layers/tree_height` | Lang, N. et al. (2023) A high-resolution canopy height model of the Earth. *Nature Ecology & Evolution* 7: 1778–1789 (ETH Global Canopy Height 2020) | CC BY 4.0 |
| `layers/tree_cover_2000` | Hansen, M. C. et al. (2013) High-resolution global maps of 21st-century forest cover change. *Science* 342: 850–853 (v1.13) | CC BY 4.0 |
| `layers/ndvi` | USGS Landsat 5 dan 7 Collection 2 surface reflectance, 2005–2009, via Google Earth Engine | domain publik |
| `layers/temperature`, `rainfall`, `sources/chelsa_bio12_rainfall.tif` | Karger, D. N. et al. (2017) Climatologies at high resolution for the earth's land surface areas. *Scientific Data* 4: 170122 (CHELSA V2.1, 1981–2010) | CC BY 4.0 |
| `layers/population` | WorldPop (www.worldpop.org), 2005, 100 m | CC BY 4.0 |
| `layers/night_lights` | NOAA National Centers for Environmental Information, DMSP-OLS Nighttime Lights Time Series, 2005 | domain publik |
| `boundaries/java.gpkg` | COD-AB Indonesia (BPS), via [HDX](https://data.humdata.org) | CC BY-IGO |
| `gbif/hylobates_moloch_gbif.csv`, `occurrences/gbif_maxent.csv` | rekaman kejadian *Hylobates moloch* dari GBIF.org (kueri API 2026-10-14); lisensi tiap rekaman ada di kolom `license`: 19 CC0, 35 CC BY 4.0, 120 CC BY-NC 4.0 (iNaturalist) | per rekaman — rekaman CC BY-NC hanya boleh dipakai untuk tujuan non-komersial |
| `bias/bias_mammals.asc` | dibuat untuk kursus ini dari 1.153 rekaman mamalia GBIF.org (1990–2026), dihaluskan dan diskalakan | mengikuti rekaman GBIF (campuran CC0 / CC BY / CC BY-NC): pemakaian non-komersial |
| `scripts/correlation.py`, `glossary.md`, `README.md`, `README.id.md` | sigro.id | CC BY 4.0 |

Semua grid telah direproyeksi dan di-resample ke grid kursus (UTM 48S, 100 m; grid Jawa 250 m) untuk kursus ini.
Konsep dalam kursus mengikuti Merow, C., Smith, M. J. dan Silander, J. A. (2013) A practical guide to MaxEnt for
modeling species' distributions: what it does, and why inputs and settings matter. *Ecography* 36: 1058–1069.
