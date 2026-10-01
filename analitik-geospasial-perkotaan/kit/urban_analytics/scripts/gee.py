"""Inisialisasi Google Earth Engine.

Dua cara:
- Akun pribadi: jalankan `earthengine authenticate` sekali, lalu isi EE_PROJECT dengan ID proyek Cloud Anda.
- Service account: isi EE_KEY dengan path berkas JSON kunci (jangan pernah membagikan atau meng-commit berkas ini).
"""
import json
import os

import ee
import geopandas as gpd


def init():
    key = os.environ.get("EE_KEY")
    if key:
        info = json.load(open(key))
        ee.Initialize(ee.ServiceAccountCredentials(info["client_email"], key), project=info["project_id"])
    else:
        ee.Initialize(project=os.environ.get("EE_PROJECT"))
    return ee


def to_ee(gdf, simplify_m=20, cols=()):
    """GeoDataFrame → ee.FeatureCollection (geometri disederhanakan agar muatan permintaan kecil)."""
    g = gdf[list(cols) + ["geometry"]].copy()
    utm = g.estimate_utm_crs()
    g["geometry"] = g.to_crs(utm).simplify(simplify_m).to_crs(4326)
    return ee.FeatureCollection(json.loads(g.to_json(drop_id=True)))


def luas_per_kelas(img, geom, scale, nama_kelas):
    """Luas (ha) per nilai kelas pada citra kelas tunggal."""
    area = ee.Image.pixelArea().divide(1e4).addBands(img.rename("kelas"))
    res = area.reduceRegion(ee.Reducer.sum().group(groupField=1, groupName="kelas"), geom, scale,
                            maxPixels=1e10).getInfo()["groups"]
    return {nama_kelas[g["kelas"]]: round(g["sum"], 1) for g in res}
