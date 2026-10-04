# GIS untuk Penyusun dan Penilai AMDAL — data latihan

Kursus: https://sigro.id/course/gis-penyusun-penilai-amdal

Unduh: [`gis-penyusun-penilai-amdal-data.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/gis-penyusun-penilai-amdal-v1/gis-penyusun-penilai-amdal-data.zip) (100 MB). Ekstrak; Anda mendapat folder `amdal/` berisi `data/` dan `LISENSI.md`.

> Rencana kegiatan (tapak, jalan angkut, titik buangan) **FIKTIF** — data latihan, bukan rencana nyata. Data
> lingkungannya nyata.

| Berkas | Isi | Pelajaran |
|---|---|---|
| `amdal_boja.gpkg` (EPSG:32749) | rencana_tapak, rencana_jalan_angkut, titik_buangan (FIKTIF); sungai, jalan, permukiman, sekolah, fasilitas_kesehatan, tempat_ibadah, mata_air, tambang_eksisting (OSM); desa (HDX/BPS) | B1–B6 |
| `amdal_boja_hasil_b2.gpkg` | hasil B2: batas proyek, ekologis, sosial, administratif, wilayah studi; zona_dampak; patok_blorong | B4–B6 |
| `amdal_boja_{dem,s2,worldcover,hansen_*,worldpop}.tif` | Copernicus DEM, Sentinel-2, ESA WorldCover, Hansen GFC, WorldPop 2020 | B2, B4, B5 |
| `amdal_kaltim.gpkg` (EPSG:32750), `amdal_kaltim_*.tif` | kasus kedua, utara Samarinda: rencana tambang batubara FIKTIF; tambang_eksisting (OSM, tanpa nama perusahaan), sungai, jalan, permukiman, desa; citra, Hansen, WorldCover, DEM | B5b |

## Lisensi

OpenStreetMap (ODbL 1.0) · HDX COD-AB/BPS (CC BY-IGO) · Copernicus Sentinel dan Copernicus DEM (lisensi Copernicus,
dengan atribusi) · ESA WorldCover, Hansen GFC, WorldPop (CC BY 4.0). Rincian di `LISENSI.md`.
