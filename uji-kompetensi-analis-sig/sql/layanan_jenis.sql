-- Tabel acuan jenis fasilitas (pelajaran 2.3). Dijalankan setelah layanan_ddl.sql.
INSERT INTO layanan.jenis_fasilitas (id_jenis, nama, sektor) VALUES
    (1, 'Rumah Sakit',         'kesehatan'),
    (2, 'Puskesmas',           'kesehatan'),
    (3, 'Puskesmas Pembantu',  'kesehatan'),
    (4, 'Posyandu',            'kesehatan'),
    (5, 'Klinik',              'kesehatan'),
    (6, 'SD/MI',               'pendidikan'),
    (7, 'SMP/MTs',             'pendidikan'),
    (8, 'SMA/SMK/MA',          'pendidikan'),
    (9, 'Pendidikan lain',     'pendidikan');
