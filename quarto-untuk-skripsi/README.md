# Quarto untuk Skripsi — paket latihan

Kursus gratis di sigro.id (Firman Hadi): menulis skripsi dengan Quarto, R atau Python, dan RStudio — dari naskah dan
analisis sampai PDF berformat FEB UNDIP dan slide sidang. Mengikuti buku gratis
[*Quarto untuk Skripsi*](https://firmanhadi21.github.io/thesis-with-quarto/) (Firman Hadi, L.M. Sabri, Y. Wahyuddin).

## Unduhan (rilis `quarto-untuk-skripsi-v1`)

[`quarto-untuk-skripsi-kit.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/quarto-untuk-skripsi-v1/quarto-untuk-skripsi-kit.zip) (0,2 MB).
Ekstrak, lalu buka `skripsi/skripsi.Rproj` di RStudio.

| Berkas | Isi | Pelajaran |
|---|---|---|
| `p14-menulis.qmd` | Markdown dan YAML | 1.4 |
| `p22-angka-{r,py}.qmd` | Angka di dalam naskah (kode sebaris), data 2024 | 2.2 |
| `p23-bersih-{r,py}.qmd` | Membersihkan data | 2.3 |
| `p25-tabel-{r,py}.qmd` | Tabel, gambar, dan persamaan bernomor | 2.5 |
| `p27-sitasi.qmd`, `references.bib`, `apa.csl` | Sitasi dan daftar pustaka | 2.7 |
| `p33-regresi-{r,py}.qmd` | Regresi data panel, uji Hausman | 3.3 |
| `p35-spasial-{r,py}.qmd` | Peta koroplet, Moran's I, LISA | 3.5 |
| `p36-deret-{r,py}.qmd` | Deret waktu, menumpuk data tahun baru | 3.6 |
| `p52-galat.qmd` | Mengatasi galat (sengaja berisi tiga kesalahan) | 5.2 |
| `template-skripsi-r/`, `template-skripsi-python/` | Templat skripsi FEB UNDIP (proyek *book*), termasuk `slide-sidang.qmd` | 4.2, 4.3, 5.4 |
| `data/` | Data latihan (lihat di bawah) | semua |

Potongan kode di dokumen praktik masih kosong; diisi sambil mengikuti video. Setiap praktik analisis punya versi R
(`-r`) dan Python (`-py`) dengan langkah yang sama.

## Data

- `data_kemiskinan_jateng.csv` — 35 kabupaten/kota Jawa Tengah × 2019–2023 (175 baris): kemiskinan, PDRB per kapita,
  inflasi, pengangguran, IPM; kunci `kode_wilayah` + `tahun`.
- `data_kemiskinan_jateng_2024.csv` — kolom yang sama untuk 2024 (35 baris).
- `data_pendukung_jateng.json` — akses sanitasi dan TPAK per kabupaten/kota dan tahun.
- `data_kotor_contoh.csv` — 12 baris yang sengaja berantakan (duplikat, koma desimal, nilai mustahil) untuk pelajaran 2.3.
- `jateng.geojson` — batas kabupaten/kota Jawa Tengah.

**Data latihan (tiruan).** Angka kemiskinan dan variabel lain disimulasikan agar masuk akal untuk belajar; bukan data
resmi BPS dan tidak untuk dikutip. Ganti dengan data asli saat menyusun skripsi sungguhan.

## Sumber dan lisensi

- **Data latihan** — dari repositori buku [thesis-with-quarto](https://github.com/firmanhadi21/thesis-with-quarto), data
  sintetis.
- **Batas wilayah** — GADM (gadm.org), tingkat 2. Lisensi GADM: bebas untuk keperluan akademik dan nonkomersial;
  penggunaan komersial dan redistribusi memerlukan izin dari GADM.
- **Gaya sitasi** — `apa.csl` dari Citation Style Language styles (CC BY-SA 3.0).
- **Templat skripsi** — dari repositori buku; format mengikuti pedoman FEB UNDIP (periksa pedoman terbaru program
  studi Anda).
