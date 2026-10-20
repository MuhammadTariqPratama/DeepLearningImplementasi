# Materi 5 — HCI dan visualisasi data

## Kasus: dashboard antrean peringatan lingkungan

Petugas menerima banyak alert dan perlu melihat ringkasan, menyaring periode dan kategori, lalu membuka detail yang relevan. Dashboard harus membantu menemukan pola tanpa menyembunyikan ketidakpastian.

## Implementasi

Skrip menghasilkan satu halaman HTML mandiri berisi ringkasan, grafik tren, filter kategori, dan tabel detail. Semua data alert bersifat sintetis. Halaman memakai elemen HTML semantik, label kontrol, kontras, dan layout responsif sebagai titik awal aksesibilitas. Grafik tren memakai SVG dan JavaScript sederhana; visual tidak bergantung pada server atau paket tambahan.

## Prinsip desain yang diterapkan

- Overview ditampilkan sebelum detail; filter mempersempit daftar.
- Tren waktu menggunakan grafik garis, kategori menggunakan angka/tabel.
- Warna selalu didampingi label teks.
- Hindari menganggap skor atau kategori sebagai bukti; sediakan konteks dan tinjauan manusia.

Uji dengan pengguna nyata tetap diperlukan. Periksa keyboard navigation, screen reader, kontras, kejelasan istilah, serta apakah petugas dapat menyelesaikan tugas tanpa bantuan.

## Menjalankan

```bash
python kasus/05_hci_visualisasi/main.py
```

Buka `kasus/05_hci_visualisasi/output/dashboard.html` di browser.
