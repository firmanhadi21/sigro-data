-- fasilitas.sql — PostGIS table for the course project survei-fasilitas, synced by mergin-db-sync (init_from: db).
-- Course "Dari Ponsel ke WebGIS", lesson 4.1. On the server, in /opt/stack-survei:
--   ./scripts/psql-survei.sh < fasilitas.sql
--   ./scripts/06-dbsync-tambah.sh survei-fasilitas fasilitas fasilitas.gpkg
--
-- Same columns as the survey layer fasilitas.gpkg, so the QGIS project's form keeps working when db-sync generates
-- the GeoPackage from this table. Only geodiff-safe types: integer primary key, text, boolean, date, geometry
-- (no timestamptz). The table name "fasilitas" becomes the GeoPackage layer name.

CREATE SCHEMA IF NOT EXISTS fasilitas_modified AUTHORIZATION g3wsuite;

CREATE TABLE IF NOT EXISTS fasilitas_modified.fasilitas (
  fid           serial PRIMARY KEY,
  kategori      text NOT NULL,
  nama          text,
  kondisi       text NOT NULL,
  akses_difabel boolean DEFAULT false,
  foto          text,
  tanggal       date,
  surveyor      text,
  catatan       text,
  geom          geometry(Point, 4326)
);
ALTER TABLE fasilitas_modified.fasilitas OWNER TO g3wsuite;
CREATE INDEX IF NOT EXISTS fasilitas_geom_idx ON fasilitas_modified.fasilitas USING gist (geom);
