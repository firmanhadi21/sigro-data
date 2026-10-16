# InSAR dengan LiCSBAS — kit tutorial (Semarang)

[English](README.en.md) · Tutorial: https://sigro.id/course/insar-licsbas (versi bahasa Inggris:
https://sigro.id/course/insar-licsbas-en) · Perangkat lunak: [LiCSBAS 1.17](https://github.com/comet-licsar/LiCSBAS)
(GPL-3.0) di image Docker `ghcr.io/firmanhadi21/insar-licsbas:1.17` (LiCSBAS + JupyterLab).

Unduhan: [`insar-semarang.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/insar-licsbas-v1/insar-semarang.zip) (17 MB).

## Menjalankan

1. Pasang Docker (Windows/macOS: Docker Desktop; Linux: Docker Engine).
2. Ekstrak `insar-semarang.zip` di folder pengguna Anda.
3. Dari folder yang berisi `insar-semarang`, jalankan:

   ```
   docker run --rm -p 127.0.0.1:8888:8888 -v "$PWD/insar-semarang:/kerja" ghcr.io/firmanhadi21/insar-licsbas:1.17
   ```

   (Windows PowerShell: ganti `$PWD` dengan `${PWD}`.)
4. Buka http://localhost:8888 di peramban, lalu folder `notebooks` (bahasa Indonesia) atau `notebooks_en`
   (bahasa Inggris).

## Isi

| Folder / berkas | Isi | Praktik |
|---|---|---|
| `notebooks/`, `notebooks_en/` | satu notebook per praktik, bahasa Indonesia dan Inggris | semua |
| `127A_09749_121312/GEOCml5clip/` | frame **ascending** Sentinel-1: 259 interferogram (unwrapped phase) dan koherensinya, 2023–2024, multilook 5 × 5 (± 550 m), diklip ke Semarang (110,25–110,70 °BT, 6,85–7,15 °LS) | p41 dan seterusnya |
| `076D_09725_121107/GEOCml5clip/` | frame **descending**, 226 interferogram, wilayah dan jendela yang sama | p81 |

Isi `GEOCml5clip` adalah keluaran LiCSBAS step 02 (multilook) dan step 05 (klip), **tanpa koreksi GACOS**: GACOS
tidak punya nilai di pesisir, sehingga koreksinya menghapus piksel pesisir Semarang. Berkas `baselines` berisi baseline
tegak lurus setiap tanggal yang dihitung dari orbit presisi Sentinel-1; berkas asli LiCSAR disimpan sebagai
`baselines.licsar`. Praktik p21 mengunduh data sendiri dari COMET-LiCSAR (Juni–Juli 2024, ± 230 MB dengan GACOS).

## Sumber dan lisensi

Lihat [CREDITS.md](CREDITS.md): produk COMET-LiCSAR adalah turunan data Copernicus Sentinel-1 (terbuka, dengan ucapan
terima kasih LiCSAR yang wajib); GACOS (hanya diunduh di praktik p31, tidak ada di kit) boleh dibagikan dengan
menyebut sumbernya, tetapi tidak untuk keperluan komersial; LiCSBAS GPL-3.0; notebook dan README CC BY 4.0.
