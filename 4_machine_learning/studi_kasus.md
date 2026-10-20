# Materi 4 — Machine Learning

## Kasus: menyaring keterlambatan pembayaran

Tim keuangan ingin mengenali pelanggan yang berisiko terlambat membayar agar tim dapat menawarkan pengingat atau bantuan lebih awal.

**Label:** apakah pelanggan terlambat pada periode berikutnya. **Fitur:** lama hubungan, jumlah invoice, nilai tagihan, dan histori keterlambatan yang tersedia sebelum periode prediksi.

## Implementasi dan evaluasi

Kode membuat data sintetis tidak seimbang, membagi train/test, melatih Logistic Regression dengan imputasi dan standardisasi, lalu membandingkannya dengan prediksi kelas mayoritas. Laporan mencakup confusion matrix, precision, recall, F1, dan balanced accuracy.

## Etika dan batasan

Contoh ini tidak boleh dipakai untuk memberi skor pelanggan sungguhan. Pastikan fitur benar-benar tersedia pada saat prediksi untuk mencegah leakage. Periksa bias, kalibrasi, dampak keputusan, privasi, dan lakukan validasi pada periode baru. Recall rendah berarti banyak pelanggan berisiko terlewat; accuracy saja bisa menutupi hal itu.

## Menjalankan

```bash
python kasus/04_machine_learning/main.py
```
