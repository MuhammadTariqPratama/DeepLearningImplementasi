# Studi Kasus dan Implementasi Materi

## Tentang proyek

Repositori ini berisi enam contoh studi kasus yang menunjukkan cara menerapkan materi analisis data, komputasi berkinerja tinggi (HPC), GIS, machine learning, HCI dan visualisasi, serta AI untuk pemantauan deforestasi. Data yang digunakan dalam contoh bersifat sintetis.

## Daftar materi

| Materi | Isi | Folder |
| --- | --- | --- |
| 1. Analisis data | Analisis pendapatan, laba, margin, dan piutang | [`1_analisis_data/`](1_analisis_data/) |
| 2. HPC | Pemrosesan skenario secara paralel dan contoh job Slurm | [`2_hpc/`](2_hpc/) |
| 3. GIS | Pemeringkatan kandidat lokasi dan ekspor data GeoJSON | [`3_gis/`](3_gis/) |
| 4. Machine learning | Klasifikasi risiko keterlambatan pembayaran dan evaluasi model | [`4_machine_learning/`](4_machine_learning/) |
| 5. HCI dan visualisasi | Dashboard interaktif untuk meninjau alert lingkungan | [`5_hci_visualisasi/`](5_hci_visualisasi/) |
| 6. AI dan deforestasi | Contoh pengelompokan dugaan penyebab alert | [`6_deforestation/`](6_deforestation/) |

Setiap folder berisi `studi_kasus.md` dan kode contoh `main.py`.

## Persiapan

Gunakan Python 3.10 atau lebih baru. Contoh analisis data dan machine learning memerlukan `pandas`, `numpy`, dan `scikit-learn`. Pasang dependensi tersebut dengan:

```powershell
python -m pip install numpy pandas scikit-learn
```

## Menjalankan contoh

Jalankan perintah dari folder utama repositori:

```powershell
python .\1_analisis_data\main.py
python .\2_hpc\main.py --workers 2
python .\3_gis\main.py
python .\4_machine_learning\main.py
python .\5_hci_visualisasi\main.py
```

Hasil setiap program disimpan di folder `output` pada folder materi terkait. Dashboard dari materi HCI dapat dibuka melalui `5_hci_visualisasi/output/dashboard.html`.

### Menjalankan job HPC di klaster

`2_hpc/job.slurm` adalah contoh untuk klaster Linux yang menggunakan Slurm. Sesuaikan konfigurasi sumber daya dan lingkungan Python dengan klaster, lalu jalankan dari folder `2_hpc`:

```bash
sbatch job.slurm
```

### Status materi deforestasi

Folder `6_deforestation` berisi launcher dan dokumentasi. Launcher tersebut merujuk ke `deforestation_case.py`, tetapi berkas itu belum tersedia di repositori ini; karena itu, contoh deforestasi belum dapat dijalankan.

## Batasan

Data dan hasil contoh hanya untuk demonstrasi, bukan gambaran kondisi nyata. Skor lokasi dan keluaran model tidak boleh dianggap sebagai rekomendasi atau keputusan otomatis. Validasi dengan data yang sesuai dan penilaian ahli diperlukan sebelum penerapan nyata.
