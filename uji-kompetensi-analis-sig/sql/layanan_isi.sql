-- Mengisi skema layanan dari data sumber yang diimpor ke skema sumber (pelajaran 2.4).
-- sumber.kelurahan (kelurahan, kecamatan, geom) dan sumber.poi (amenity, name, geom), keduanya EPSG:32749.

-- 1. kecamatan: satu baris per nama kecamatan, kode dua digit menurut abjad
INSERT INTO layanan.kecamatan (kode_kec, nama)
SELECT lpad(row_number() OVER (ORDER BY kecamatan)::text, 2, '0'), kecamatan
FROM (SELECT DISTINCT kecamatan FROM sumber.kelurahan) k;

-- 2. kelurahan: kode = kode kecamatan + nomor urut tiga digit (01001, 01002, ...)
INSERT INTO layanan.kelurahan (kode_kel, nama, kode_kec, geom)
SELECT c.kode_kec || lpad(row_number() OVER (PARTITION BY c.kode_kec ORDER BY s.kelurahan)::text, 3, '0'),
       s.kelurahan, c.kode_kec, ST_Multi(s.geom)
FROM sumber.kelurahan s
JOIN layanan.kecamatan c ON c.nama = s.kecamatan;

-- 3. fasilitas: jenis dari amenity dan nama; kelurahan dari lokasi titik (NULL bila di luar batas kota)
INSERT INTO layanan.fasilitas (nama, id_jenis, kode_kel, geom)
SELECT p.name,
       CASE
           WHEN p.amenity = 'hospital' THEN 1
           WHEN p.amenity = 'clinic' AND p.name ~* 'pustu|puskesmas pembantu' THEN 3
           WHEN p.amenity = 'clinic' AND p.name ~* 'puskesmas' THEN 2
           WHEN p.amenity = 'clinic' AND p.name ~* 'posyandu' THEN 4
           WHEN p.amenity = 'clinic' THEN 5
           WHEN p.name ~* '^(SD|SDN|SDIT|MI|MIN|Sekolah Dasar)\M' THEN 6
           WHEN p.name ~* '^(SMP|SMPN|SMPIT|MTs|MTsN|SLTP)\M' THEN 7
           WHEN p.name ~* '^(SMA|SMAN|SMK|SMKN|MA|MAN|Madrasah Aliyah|SLTA)\M' THEN 8
           ELSE 9
       END,
       k.kode_kel, p.geom
FROM sumber.poi p
LEFT JOIN layanan.kelurahan k ON ST_Within(p.geom, k.geom)
WHERE p.amenity IN ('hospital', 'clinic', 'school') AND p.name IS NOT NULL;

-- 4. periksa
SELECT j.sektor, j.nama AS jenis, count(f.id) AS jumlah
FROM layanan.jenis_fasilitas j LEFT JOIN layanan.fasilitas f USING (id_jenis)
GROUP BY j.id_jenis, j.sektor, j.nama ORDER BY j.id_jenis;
