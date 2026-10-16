# InSAR with LiCSBAS — tutorial kit (Semarang)

[Bahasa Indonesia](README.md) · Tutorial: https://sigro.id/course/insar-licsbas-en (Indonesian version:
https://sigro.id/course/insar-licsbas) · Software: [LiCSBAS 1.17](https://github.com/comet-licsar/LiCSBAS) (GPL-3.0)
in the Docker image `ghcr.io/firmanhadi21/insar-licsbas:1.17` (LiCSBAS + JupyterLab).

Download: [`insar-semarang.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/insar-licsbas-v1/insar-semarang.zip) (17 MB).

## Running it

1. Install Docker (Windows/macOS: Docker Desktop; Linux: Docker Engine).
2. Unzip `insar-semarang.zip` in your home folder.
3. From the folder that contains `insar-semarang`, run:

   ```
   docker run --rm -p 127.0.0.1:8888:8888 -v "$PWD/insar-semarang:/kerja" ghcr.io/firmanhadi21/insar-licsbas:1.17
   ```

   (Windows PowerShell: use `${PWD}` instead of `$PWD`.)
4. Open http://localhost:8888 in a browser, then the `notebooks_en` folder (English; `notebooks` holds the
   Indonesian versions).

## Contents

| Folder / file | Contents | Practice |
|---|---|---|
| `notebooks_en/`, `notebooks/` | one notebook per practice, English and Indonesian | all |
| `127A_09749_121312/GEOCml5clip/` | Sentinel-1 **ascending** frame: 259 unwrapped interferograms and their coherence, 2023–2024, multilooked 5 × 5 (≈ 550 m), clipped to Semarang (110.25–110.70 °E, 6.85–7.15 °S) | p41 onward |
| `076D_09725_121107/GEOCml5clip/` | **descending** frame, 226 interferograms, same area and window | p81 |

`GEOCml5clip` is the output of LiCSBAS step 02 (multilook) and step 05 (clip), **without the GACOS correction**:
GACOS has no values on the coast, so the correction removes Semarang's coastal pixels. The `baselines` file holds the
perpendicular baseline of every date, computed from Sentinel-1 precise orbits; LiCSAR's original is kept as
`baselines.licsar`. Practice p21 downloads data from COMET-LiCSAR itself (June–July 2024, ≈ 230 MB with GACOS).

## Sources and licences

See [CREDITS.md](CREDITS.md): COMET-LiCSAR products are derived Copernicus Sentinel-1 data (open, with the required
LiCSAR acknowledgement); GACOS (downloaded in practice p31 only, not in the kit) may be shared with credit but not for
commercial use; LiCSBAS GPL-3.0; notebooks and READMEs CC BY 4.0.
