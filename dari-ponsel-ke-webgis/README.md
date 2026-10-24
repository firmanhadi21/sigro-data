# Dari Ponsel ke WebGIS — paket kursus

Tutorial: https://sigro.id/course/dari-ponsel-ke-webgis · Survei lapangan dengan Mergin Maps, data ke PostGIS dengan
mergin-db-sync, peta web dengan G3W-Suite, semuanya di server sendiri.

Unduhan (rilis `dari-ponsel-ke-webgis-v1`):

| Berkas | Isi | Dipakai di |
|---|---|---|
| [`survei-fasilitas.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/dari-ponsel-ke-webgis-v1/survei-fasilitas.zip) (0,6 MB) | paket latihan: `peta_dasar.gpkg` (batas kampus UNDIP Tembalang, bangunan, jalan), `fasilitas_simbol.qml` (simbol 10 kategori fasilitas), `BACA_SAYA.txt` | modul 1 (pelajaran 1.1–1.3) |
| [`stack-survei.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/dari-ponsel-ke-webgis-v1/stack-survei.zip) (0,05 MB) | kit server: Mergin Maps CE 2025.7.3, G3W-Suite (QGIS Server 3.44) + PostGIS, mergin-db-sync, nginx + Let's Encrypt, skrip pemasangan `00`–`06`, cadangan, `foto_sync.sh`; panduan di `stack-survei/README.md` | modul 4 dan 6 |

## Kit server singkatnya

Butuh VPS **x86-64** (bukan ARM) dengan Ubuntu 22.04/24.04, disarankan 4 vCPU / 8 GB RAM, dua nama host dengan
catatan A ke IP server, dan login SSH sebagai pengguna biasa dengan `sudo`. Di server:

```bash
sudo apt install -y unzip
wget https://github.com/firmanhadi21/sigro-data/releases/download/dari-ponsel-ke-webgis-v1/stack-survei.zip
unzip stack-survei.zip
sudo mv stack-survei /opt/ && sudo chown -R "$USER" /opt/stack-survei
cd /opt/stack-survei && cp .env.example .env    # lalu isi DOMAIN, MAPS_DOMAIN, CONTACT_EMAIL
```

Langkah berikutnya (`00-bootstrap` sampai `05-dbsync-setup`) ada di `stack-survei/README.md`.

## Sumber dan lisensi

- Data peta dasar: © kontributor OpenStreetMap, [ODbL 1.0](https://www.openstreetmap.org/copyright).
- Kit diturunkan dari tumpukan yang menjalankan [ownmap.id](https://github.com/firmanhadi21/ownmap.id). Perangkat
  lunak yang dijalankannya punya lisensi sendiri: Mergin Maps CE (Lutra Consulting, AGPL-3.0), mergin-db-sync
  (Lutra Consulting, MIT), G3W-Suite (Gis3w, MPL-2.0; berkas konfigurasi di `g3w-suite/config/` berasal dari
  g3w-suite-docker dan tetap MPL-2.0), nginx, Let's Encrypt/certbot.
- Skrip, berkas konfigurasi lain, README, dan simbol QML: Firman Hadi, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
