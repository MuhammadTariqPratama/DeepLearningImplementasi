# Materi 1 — Mengubah data menjadi keputusan

## Kasus: laba turun saat pendapatan naik

PT Contoh Niaga melaporkan pendapatan meningkat, tetapi laba bersih turun dan piutang membesar. Pimpinan ingin mengetahui apakah penurunan laba berasal dari margin yang menyusut, biaya yang naik, atau piutang yang menua.

**Pertanyaan bisnis:** tindakan apa yang perlu diselidiki manajemen pada kuartal ini?

**Pertanyaan analitik:** bagaimana pendapatan, laba, margin, dan piutang berubah per kuartal; pelanggan mana yang menyumbang piutang lewat jatuh tempo?

## Pendekatan

Kode membuat data sintetis tingkat transaksi dan snapshot piutang. Ia memeriksa nilai yang hilang dan duplikasi, menghitung ringkasan per kuartal, lalu mengurutkan piutang lewat jatuh tempo. Transaksi dan piutang tidak dijoin langsung karena granularitasnya berbeda; agregasi dilakukan terpisah agar nilai tidak terduplikasi.

## Keputusan yang didukung dan batasan

Laporan memberi sinyal untuk memeriksa margin dan penagihan. Angka tidak membuktikan sebab-akibat. Contoh data tidak mewakili perusahaan nyata; sebelum tindakan, validasi definisi laba, tanggal jatuh tempo, retur, pajak, dan kebijakan akuntansi dengan pemilik data.

## Menjalankan

```bash
python kasus/01_analisis_data/main.py
```

Hasil CSV ditulis ke `kasus/01_analisis_data/output/`.
