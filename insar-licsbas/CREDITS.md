# Sources and licences / Sumber dan lisensi

| Files | Source | Licence / terms |
|---|---|---|
| `*/GEOCml5clip/20*_20*/` (unwrapped interferograms, coherence), `*.geo` (E, N, U), `hgt`, `slc.mli`, `baselines.licsar` | COMET-LiCSAR products of frames 127A_09749_121312 and 076D_09725_121107, 2023–2024, multilooked and clipped with LiCSBAS for this tutorial | Derived Works of Copernicus Sentinel-1 data, free and open; acknowledgement below |
| `*/GEOCml5clip/baselines` | perpendicular baselines of every date, computed for this tutorial from Copernicus Sentinel-1 precise orbit files (POEORB), via the ESA STEP server, against LiCSAR's reference date (LiCSAR's own file: `baselines.licsar`) | Copernicus Sentinel data, free and open |
| `notebooks/`, `README*.md`, `CREDITS.md` | sigro.id | CC BY 4.0 |

**Acknowledgement required by LiCSAR:** "LiCSAR contains modified Copernicus Sentinel data [2023–2024] analysed by
the Centre for the Observation and Modelling of Earthquakes, Volcanoes and Tectonics (COMET). LiCSAR uses JASMIN,
the UK's collaborative data analysis environment."

- Lazecký, M. et al. (2020) LiCSAR: An Automatic InSAR Tool for Measuring and Monitoring Tectonic and Volcanic
  Activity. *Remote Sensing* 12: 2430. doi:10.3390/rs12152430
- Morishita, Y. et al. (2020) LiCSBAS: An Open-Source InSAR Time Series Analysis Package Integrated with the LiCSAR
  Automated Sentinel-1 InSAR Processor. *Remote Sensing* 12: 424. doi:10.3390/rs12030424 — LiCSBAS, GPL-3.0.

**GACOS** (practice p31 only; not in this kit): downloaded by LiCSBAS step 01 from COMET-LiCSAR. Users may share
GACOS data with credit, but not for commercial purposes. Cite Yu, C., Li, Z., Penna, N. T., Crippa, P. (2018)
Generic atmospheric correction model for Interferometric Synthetic Aperture Radar observations. *Journal of
Geophysical Research: Solid Earth* 123: 9202–9222. doi:10.1029/2017JB015305

Concepts in the tutorial follow Berardino, P. et al. (2002) *IEEE TGRS* 40: 2375–2383 (SBAS) and López-Quiroz, P.
et al. (2009) *Journal of Applied Geophysics* 69: 1–15 (NSBAS); Semarang subsidence: Abidin, H. Z. et al. (2013)
*Geomatics, Natural Hazards and Risk* 4: 226–240.
