# Species Distribution Modelling with Maxent — course kit

[Bahasa Indonesia](README.id.md) · Course: https://sigro.id/course/maxent-sdm · Software: [Maxent 3.4.4](https://github.com/mrmaxent/Maxent) (MIT),
[QGIS](https://qgis.org) 3.40 or later, Java 11 or later.

Downloads: [`maxent-sdm.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/maxent-sdm-v1/maxent-sdm.zip) (87 MB) · [`maxent-sdm-java.zip`](https://github.com/firmanhadi21/sigro-data/releases/download/maxent-sdm-v1/maxent-sdm-java.zip) (31 MB, for module M10).

Unzip `maxent-sdm.zip` in your home folder: you get a folder `maxent-course/` (Windows
`C:\Users\<name>\maxent-course`, macOS/Linux `~/maxent-course`). The videos use exactly these paths. For module M10,
unzip `maxent-sdm-java.zip` in the same place: it adds `maxent-course/layers_java/`.

Study area: **Banten and Jawa Barat**, Indonesia. All grids: **UTM zone 48S (EPSG:32748), 100 m**, 4,165 × 2,261
cells, ESRI ASCII (`.asc`), nodata −9999 (the sea and areas outside the study area).

| Folder / file | Contents | Practice |
|---|---|---|
| `layers/*.asc` | 14 environmental grids (table below) | p31, p32, p51 – p91 |
| `layers_java/*.asc` | the 10 layers used in the model, for all of Java at 250 m | p101 |
| `bias/bias_mammals.asc` | target-group sampling-effort grid from GBIF mammal records (1–100) | p82 |
| `gbif/hylobates_moloch_gbif.csv` | the GBIF records of the Javan gibbon, as downloaded (174 rows, uncleaned) | p21 |
| `occurrences/gbif_maxent.csv` | the 6 clean GBIF localities as Maxent reads them: `species,x,y` in UTM 48S | p51 onward, your exercises |
| `boundaries/java.gpkg` | layers `java` (outline) and `study_area` (Banten + Jawa Barat), UTM 48S | p21, p22 |
| `sources/chelsa_bio12_rainfall.tif` | CHELSA annual rainfall, 30 arc-seconds, longitude/latitude: the raw input of `layers/rainfall.asc` | p31 |
| `scripts/correlation.py` | Pearson correlation between the layers at 10,000 random land cells | p32 |
| `output/` | empty: make one folder per Maxent or QGIS run here | all |
| `glossary.md` | the terms used in the course | — |

## The layers

| File | Variable | Source, year | Note |
|---|---|---|---|
| `elevation` | elevation, m | SRTM, 2000 | dropped from the model (r = −0.99 with temperature) |
| `slope` | slope, degrees | from SRTM | |
| `northness`, `eastness` | cos and sin of aspect | from SRTM | aspect is circular |
| `dist_river`, `dist_road` | distance to the nearest river / road, m | OpenStreetMap (Geofabrik extract, 2026-10-12) | today's roads, not those of the record years |
| `forest_function` | forest-area function, 5 classes: 1 conservation area, 2 protection forest (HL), 3 production forest (HP/HPT), 4 convertible (HPK, absent here), 5 other land use (APL) | KLHK, Penunjukan Kawasan Hutan 1:250,000 | **categorical** in Maxent |
| `tree_height` | canopy height, m | ETH Global Canopy Height 2020 | |
| `tree_cover_2000` | tree cover, % | Hansen Global Forest Change v1.13 | dropped (r = 0.79 with tree height) |
| `ndvi` | median NDVI 2005–2009 | Landsat 5 and 7 | dropped (r = 0.78 with tree height) |
| `temperature` | mean annual temperature, °C | CHELSA 2.1, 1981–2010 | |
| `rainfall` | annual precipitation, mm | CHELSA 2.1, 1981–2010 | |
| `population` | people per 100 m cell | WorldPop, 2005 | |
| `night_lights` | stable night lights, DN | DMSP-OLS, 2005 | dropped (r = 0.80 with population) |

## About the occurrence records

The videos model **field records of the Javan gibbon** (Iskandar, Nursal, and the Sancang and Priangan surveys,
1992–2009). The Javan gibbon is endangered and hunted for the pet trade, so **those records are not in this kit**,
and nothing derived from them is either. The kit gives you the public **GBIF** records instead: practice p21 cleans
them, p22 turns them into `occurrences/gbif_maxent.csv`.

Six clean localities are far too few for a reliable model — with fewer than ten records Maxent uses linear features
only — and that is part of the lesson: record quality limits a model more than any setting. Use them to practise
every step, compare your numbers with the videos' to see what more and better records change, and add records from
your own surveys where you can (keep the locations of threatened species private).



## Sources and licences

Please cite the sources whenever you use or share these files.

| Files | Source | Licence |
|---|---|---|
| `layers/elevation`, `slope`, `northness`, `eastness`; Java versions | NASA SRTM (2000), via Google Earth Engine | public domain |
| `layers/dist_river`, `dist_road` | © OpenStreetMap contributors, Geofabrik extract of Java (2026-10-12) | [ODbL 1.0](https://www.openstreetmap.org/copyright) — the distance grids are a produced work: attribute OpenStreetMap |
| `layers/forest_function` | Kementerian Lingkungan Hidup dan Kehutanan (KLHK), *Penunjukan Kawasan Hutan* 1:250,000, grouped into 5 classes | government data, credited to KLHK |
| `layers/tree_height` | Lang, N. et al. (2023) A high-resolution canopy height model of the Earth. *Nature Ecology & Evolution* 7: 1778–1789 (ETH Global Canopy Height 2020) | CC BY 4.0 |
| `layers/tree_cover_2000` | Hansen, M. C. et al. (2013) High-resolution global maps of 21st-century forest cover change. *Science* 342: 850–853 (v1.13) | CC BY 4.0 |
| `layers/ndvi` | USGS Landsat 5 and 7 Collection 2 surface reflectance, 2005–2009, via Google Earth Engine | public domain |
| `layers/temperature`, `rainfall`, `sources/chelsa_bio12_rainfall.tif` | Karger, D. N. et al. (2017) Climatologies at high resolution for the earth's land surface areas. *Scientific Data* 4: 170122 (CHELSA V2.1, 1981–2010) | CC BY 4.0 |
| `layers/population` | WorldPop (www.worldpop.org), 2005, 100 m | CC BY 4.0 |
| `layers/night_lights` | NOAA National Centers for Environmental Information, DMSP-OLS Nighttime Lights Time Series, 2005 | public domain |
| `boundaries/java.gpkg` | Indonesia COD-AB (BPS), via [HDX](https://data.humdata.org) | CC BY-IGO |
| `gbif/hylobates_moloch_gbif.csv`, `occurrences/gbif_maxent.csv` | GBIF.org occurrence records of *Hylobates moloch* (API query of 2026-10-14); the licence of each record is in its `license` column: 19 CC0, 35 CC BY 4.0, 120 CC BY-NC 4.0 (iNaturalist) | per record — the CC BY-NC records may be used for non-commercial purposes only |
| `bias/bias_mammals.asc` | made for this course from 1,153 GBIF.org mammal occurrence records (1990–2026), smoothed and scaled | follows the GBIF records (mixed CC0 / CC BY / CC BY-NC): non-commercial use |
| `scripts/correlation.py`, `glossary.md`, `README.md` | sigro.id | CC BY 4.0 |

All grids were reprojected and resampled onto the course grid (UTM 48S, 100 m; Java grid 250 m) for this course.
Concepts in the course follow Merow, C., Smith, M. J. and Silander, J. A. (2013) A practical guide to MaxEnt for
modeling species' distributions: what it does, and why inputs and settings matter. *Ecography* 36: 1058–1069.
