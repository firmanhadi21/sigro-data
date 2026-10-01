-- Basis data layanan kesehatan dan pendidikan Kota Semarang (pelajaran 2.2 model fisik, 2.3–2.5 praktik).
-- PostgreSQL 17 + PostGIS 3.5. Sistem koordinat: WGS 84 / UTM zona 49S (EPSG:32749).
CREATE SCHEMA IF NOT EXISTS layanan;

CREATE TABLE layanan.kecamatan (
    kode_kec  varchar(4) PRIMARY KEY,
    nama      text NOT NULL UNIQUE
);

CREATE TABLE layanan.kelurahan (
    kode_kel  varchar(5) PRIMARY KEY,
    nama      text NOT NULL,
    kode_kec  varchar(4) NOT NULL REFERENCES layanan.kecamatan (kode_kec),
    geom      geometry(MultiPolygon, 32749) NOT NULL
);

CREATE TABLE layanan.jenis_fasilitas (
    id_jenis  smallint PRIMARY KEY,
    nama      text NOT NULL UNIQUE,
    sektor    text NOT NULL CHECK (sektor IN ('kesehatan', 'pendidikan'))
);

CREATE TABLE layanan.fasilitas (
    id        serial PRIMARY KEY,
    nama      text NOT NULL,
    id_jenis  smallint NOT NULL REFERENCES layanan.jenis_fasilitas (id_jenis),
    kode_kel  varchar(5) REFERENCES layanan.kelurahan (kode_kel),
    geom      geometry(Point, 32749) NOT NULL
);

CREATE INDEX kelurahan_geom_idx ON layanan.kelurahan USING gist (geom);
CREATE INDEX fasilitas_geom_idx ON layanan.fasilitas USING gist (geom);
