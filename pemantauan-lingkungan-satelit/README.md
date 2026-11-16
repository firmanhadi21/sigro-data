# Pemantauan Lingkungan dari Satelit — paket kursus

Kursus: https://sigro.id/course/pemantauan-lingkungan-satelit · Perangkat: [earthchange](https://github.com/firmanhadi21/rs-change-detection)
**0.3.1** (MIT)

Unduh: [`pemantauan-lingkungan-satelit-kit.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/pemantauan-lingkungan-satelit-v2/pemantauan-lingkungan-satelit-kit.zip).
Ekstrak; Anda mendapat folder `kerja/` — folder kerja yang dipakai di semua video.

| Berkas | Isi | Pelajaran |
|---|---|---|
| `environment.yml` | lingkungan Miniforge/conda (conda-forge, Python 3.12, `earthchange==0.3.1`) untuk Windows (Git Bash) dan alternatif Docker | 1.3 |
| `data/zona_fiktif_ketapang.gpkg` | zona fungsi kawasan hutan **FIKTIF** untuk Kabupaten Ketapang (kolom `FUNGSI_HTN`): kotak-kotak di atas batas kabupaten, bukan fungsi kawasan resmi | 7.2, 10.2 |

Data citra dan iklim **tidak** ada di paket ini: earthchange mengambilnya sendiri dari Microsoft Planetary Computer (tanpa
akun) dan Google Earth Engine (akun Anda sendiri, bagian 4). Simpan kunci Earth Engine Anda sebagai `kerja/ee-key.json`;
jangan pernah membagikannya.

## Memasang

- **Windows:** Git for Windows (Git Bash) + Miniforge, lalu di Git Bash: `cd ~/kerja`, `conda env create -f environment.yml`,
  `conda activate earthchange`, `earthchange --list` (pelajaran 1.3).
- **macOS/Linux:** `docker run --rm -it -v "$PWD:/kerja" ghcr.io/firmanhadi21/earthchange:0.3.1` dari dalam folder `kerja`
  (pelajaran 1.4), atau `environment.yml` yang sama dengan Miniforge.

## Lisensi

Zona FIKTIF: dibuat untuk kursus ini (CC BY 4.0, sigro.id). Batas kabupaten di dalamnya: FAO. 2025. Global Administrative
Unit Layers (GAUL). https://data.apps.fao.org. Licence: CC-BY-4.0. earthchange: MIT.
