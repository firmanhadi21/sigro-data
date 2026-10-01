# Analitik Geospasial Perkotaan — paket latihan

Pipeline analitik perkotaan yang bisa dijalankan ulang untuk kota mana pun di Indonesia: dari data terbuka
sampai dasbor. Kota aktif ditentukan oleh **`city_config.json`** (salin dari `config/<kota>.json`).

## Mulai

```bash
conda create -n urban-geo python=3.11 -y && conda activate urban-geo
conda install -c conda-forge gdal -y        # ogr2ogr, gdalwarp
pip install -r requirements.txt
cp config/semarang.json city_config.json
python scripts/fetch_osm.py                  # snapshot sudah ada di paket; --unduh-ulang untuk data OSM terbaru
python scripts/fetch_ghlc.py                 # tutupan lahan GHLC 2020–2024
python scripts/buat_tabel.py                 # tabel latihan notebook 01
jupyter lab
```

Paket ini sudah berisi snapshot Semarang dan Makassar yang dipakai di video (`data/raw/<kota>/snapshot.json`), sehingga
angka Anda sama dengan angka di video. Mengunduh ulang dari OSM bisa memberi angka yang sedikit berbeda.

## Isi

| Notebook | Topik |
|---|---|
| 00 | Persiapan dan `city_config.json` |
| 01 | Python dan pandas |
| 02 | Akuisisi data: Overpass API dengan cache, scraping etis |
| 04 | GeoPandas dan morfologi kota |
| 05 | KDB, KLB, dan kepatuhan zonasi (zonasi sintetis) |
| 06 | Indeks spasial H3 |
| 07 | Jaringan jalan dengan OSMnx |
| 08 | Space syntax dan aksesibilitas jaringan |
| 09 | PostGIS (butuh `DATABASE_URL`) |
| 10 | Tutupan lahan dan perubahannya: GEE + GHLC |
| 11 | Risiko pesisir di GEE |
| 12 | Lalu lintas dan mobilitas (data sintetis) |
| `app/dasbor.py` | Dasbor Streamlit: `streamlit run app/dasbor.py` |
| `scripts/jalankan_pipeline.py` | Seluruh pipeline untuk kota lain: `python scripts/jalankan_pipeline.py config/makassar.json` |

Earth Engine (notebook 10–11): jalankan `earthengine authenticate` dan isi `EE_PROJECT` dengan ID proyek Cloud
Anda, atau isi `EE_KEY` dengan path kunci *service account*. Jangan pernah membagikan atau meng-commit kunci itu.

## Data sintetis

Batas zonasi (KDB/KLB maksimum per zona), perjalanan ojol, dan kecepatan lalu lintas **dibangkitkan untuk
latihan**. Semuanya diberi label sintetis dan tidak menggambarkan kondisi kota yang sebenarnya. Laju penurunan
tanah di notebook 11 juga ilustratif, bukan hasil pengukuran.

## Sumber data dan atribusi

- **OpenStreetMap** — © kontributor OpenStreetMap, lisensi ODbL 1.0 (batas wilayah, bangunan, jalan, POI).
  Data turunan dari OSM (misalnya `blok.gpkg`) tetap berlisensi ODbL.
- **Global Harmonized Land Cover (GHLC)** — OpenGeoHub / LandMetric; Moreno et al. (2026),
  https://doi.org/10.5194/egusphere-2026-5540; data: https://source.coop/opengeohub/ogh-ghlc10
- **ESA WorldCover 2021 v200** — © ESA WorldCover project, CC BY 4.0.
- **Copernicus DEM GLO-30** — © DLR e.V. 2010–2014 dan © Airbus Defence and Space GmbH 2014–2018, disediakan
  di bawah program COPERNICUS oleh Uni Eropa dan ESA.
- **Landsat 5, 8, 9 Collection 2** — courtesy of the U.S. Geological Survey.
- **Wikipedia bahasa Indonesia** — tabel kecamatan, CC BY-SA 4.0.
