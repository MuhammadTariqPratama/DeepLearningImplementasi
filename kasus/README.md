# Studi Kasus dan Implementasi per Materi

Paket ini menerjemahkan enam materi dalam `rangkuman.txt` menjadi kasus belajar dan prototipe yang dapat dijalankan. Semua data buatan ditandai sebagai sintetis; hasilnya untuk pembelajaran, bukan keputusan bisnis, kredit, atau penegakan hukum.

## Daftar materi

| Materi | Studi kasus dan kode | Cara menjalankan |
|---|---|---|
| 1. Analisis data dan AI | [Kasus](01_analisis_data/studi_kasus.md), [kode](01_analisis_data/main.py) | `python kasus/01_analisis_data/main.py` |
| 2. HPC dan tantangan lokal | [Kasus](02_hpc/studi_kasus.md), [kode](02_hpc/main.py), [contoh job Slurm](02_hpc/job.slurm) | `python kasus/02_hpc/main.py --workers 2` |
| 3. GIS dan karier industri | [Kasus](03_gis/studi_kasus.md), [kode](03_gis/main.py) | `python kasus/03_gis/main.py` |
| 4. Machine learning | [Kasus](04_machine_learning/studi_kasus.md), [kode](04_machine_learning/main.py) | `python kasus/04_machine_learning/main.py` |
| 5. HCI dan visualisasi | [Kasus](05_hci_visualisasi/studi_kasus.md), [kode](05_hci_visualisasi/main.py) | `python kasus/05_hci_visualisasi/main.py` lalu buka `output/dashboard.html` |
| 6. AI untuk alert deforestasi | [Kasus](06_deforestation/studi_kasus.md), [kode utama](../deforestation_case.py), [launcher](06_deforestation/main.py) | `python kasus/06_deforestation/main.py --generate-demo --output-dir kasus/06_deforestation/output` |

## Persiapan

Materi 2, 3, dan 5 hanya memakai pustaka standar Python. Materi 1 memakai pandas; materi 4 dan 6 memakai pandas, NumPy, dan scikit-learn. Semuanya tercantum di `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Jalankan perintah dari direktori utama repositori. Contoh output disimpan ke folder `output` di direktori kasus masing-masing. Untuk HPC, skrip Python bisa dicoba lokal; file Slurm menunjukkan pola pengiriman job ke klaster yang benar-benar menyediakan Slurm. Di klaster, dari folder `kasus/02_hpc`, sesuaikan konfigurasi lalu jalankan `sbatch job.slurm`.

## Alur belajar

Mulai dari pertanyaan dan pengguna, periksa data, buat baseline sederhana, evaluasi dengan metrik yang sesuai, lalu jelaskan batasan sebelum menyarankan tindakan. Jangan mengirim data pribadi atau lokasi sensitif ke AI eksternal tanpa otorisasi dan anonimisasi.
