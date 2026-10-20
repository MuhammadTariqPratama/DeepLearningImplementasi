# Materi 2 — HPC untuk masalah lokal

## Kasus: pemetaan risiko panas dan kebutuhan pendinginan

Pemda ingin menguji banyak kombinasi skenario suhu, tutupan lahan, dan kapasitas pendinginan untuk menemukan kecamatan yang perlu dikaji lebih dulu. Penghitungan tiap skenario dapat dibagi, dijalankan serentak, lalu hasilnya digabung.

**Pertanyaan analitik:** bagaimana skor paparan berubah antar-skenario dan area, dan berapa biaya komputasi untuk memperluas resolusi?

## Implementasi dan alur HPC

`main.py` mendemonstrasikan pemecahan skenario menjadi beberapa tugas CPU lokal dengan `ProcessPoolExecutor`. `job.slurm` menunjukkan bentuk batch job pada klaster Slurm: minta sumber daya, aktifkan lingkungan, lalu jalankan skrip. Ini contoh edukatif; bukan model iklim atau hasil pemetaan resmi.

Alur klaster umumnya: siapkan data dan SSH key, masuk ke login node, unggah kode, ajukan job melalui scheduler, pantau status, unduh hasil. Jangan menjalankan beban komputasi besar di login node.

## Peran integrator dan batasan

Analis komputasi perlu bekerja bersama ahli iklim, GIS, dan pemerintah lokal untuk menentukan asumsi serta memeriksa hasil. Skor contoh tidak boleh dipakai untuk mengalokasikan bantuan nyata tanpa data terukur, validasi, dan penilaian ahli.

## Menjalankan

```bash
python kasus/02_hpc/main.py --workers 2
```

Pada klaster Slurm, sesuaikan akun, partisi, modul Python, dan lokasi data di `job.slurm`, lalu dari folder `kasus/02_hpc` jalankan `sbatch job.slurm`.
