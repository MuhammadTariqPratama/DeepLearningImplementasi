# Materi 3 — GIS sebagai pemecahan masalah industri

## Kasus: memilih lokasi gerai layanan

Tim ekspansi ingin menyaring kandidat lokasi gerai berdasarkan populasi sekitar dan jarak ke jalan utama, pesaing, serta fasilitas transit. GIS membantu menggabungkan lokasi dan atribut menjadi gambaran yang dapat ditinjau tim bisnis.

**Pertanyaan analitik:** kandidat mana yang layak dikaji lebih lanjut menurut kriteria awal?

## Implementasi

Kode menggunakan koordinat sintetis dan rumus Haversine untuk menghitung jarak. Skor adalah aturan transparan yang memberi bobot populasi, akses jalan, jarak pesaing, dan transit. CSV kandidat serta GeoJSON dihasilkan agar dapat dibuka pada QGIS.

## Batasan

Skor bukan rekomendasi investasi. Lokasi sintetis tidak merepresentasikan kota tertentu. Penerapan nyata perlu data terbuka yang mutakhir, sistem koordinat tervalidasi, waktu tempuh jaringan jalan, zonasi, sewa, survei lapangan, izin, dan analisis dampak. Portofolio GIS yang baik juga menjelaskan proses dan asumsi, bukan hanya peta akhir.

## Menjalankan

```bash
python kasus/03_gis/main.py
```
