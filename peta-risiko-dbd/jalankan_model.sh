#!/bin/bash
# Menjalankan Model Risiko DBD Semarang dari terminal (QGIS 3.34 atau lebih baru; diuji di QGIS 4.2).
# Windows: jalankan dari OSGeo4W Shell (ganti "\" di akhir baris dengan "^").
# macOS: QGIS_PROCESS=/Applications/QGIS.app/Contents/MacOS/qgis_process bash jalankan_model.sh
MODEL=model_risiko_dbd_semarang.model3
D=dbd_semarang.gpkg
mkdir -p hasil
"${QGIS_PROCESS:-qgis_process}" run "$MODEL" -- \
  kelurahan="$D|layername=kelurahan" kasus="$D|layername=kasus_dbd_2025" \
  puskesmas="$D|layername=puskesmas" stasiun="$D|layername=stasiun_hujan" \
  field_penduduk=penduduk field_pkm=nama_pkm field_ch=ch_tahunan dem=dem_semarang_30m.tif \
  radius_kde=1000 ukuran_piksel=50 \
  bobot_ir=0.30 bobot_kde=0.25 bobot_ch=0.15 bobot_elev=0.15 bobot_akses=0.15 \
  heatmap_kasus_dbd=hasil/heatmap.tif curah_hujan_idw=hasil/ch_idw.tif \
  laporan_nearest_neighbour=hasil/nna.html \
  kasus_dbd_teranalisis=hasil/kasus_teranalisis.gpkg kelurahan_risiko_dbd=hasil/kelurahan_risiko.gpkg
