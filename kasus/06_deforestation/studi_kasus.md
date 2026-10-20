# Materi 6 — AI untuk mengelompokkan penyebab alert deforestasi

## Kasus

Petugas menerima peringatan perubahan tutupan hutan, tetapi alert hanya menunjukkan lokasi gangguan, belum penyebabnya. Prototipe mengelompokkan kemungkinan penyebab dari fitur perubahan vegetasi, radar, kebakaran, bentuk area, dan jarak ke jalan atau sungai. Keluaran membantu menyusun antrean pemeriksaan; bukan bukti pelanggaran.

## Implementasi

Implementasi lengkap ada di [deforestation_case.py](../../deforestation_case.py). Launcher `main.py` pada folder ini memanggil program yang sama. Program membuat data sintetis bila diminta, membandingkan model Random Forest dengan baseline kelas mayoritas, menghitung metrik per kelas, dan menandai prediksi berkeyakinan rendah untuk tinjauan manusia.

## Menjalankan

Dari direktori utama proyek, pasang dependensi jika belum tersedia lalu jalankan:

```powershell
python -m pip install -r requirements.txt
python kasus/06_deforestation/main.py --generate-demo --output-dir kasus/06_deforestation/output
```

Metrik, confusion matrix, dan antrean tinjauan akan disimpan di folder output tersebut. Untuk memakai data sendiri, lihat petunjuk dan skema CSV pada [studi kasus utama](../../studi_kasus.md).

## Batasan

Data demo sepenuhnya sintetis dan tidak mengukur kinerja untuk hutan atau lokasi nyata. Untuk penerapan, gunakan label terverifikasi, pemisahan train/test berdasarkan lokasi atau waktu, tinjauan ahli, serta data lapangan. Jangan memakai prediksi model sebagai dasar tunggal penegakan hukum.
