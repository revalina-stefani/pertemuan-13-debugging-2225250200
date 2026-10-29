
# Pertemuan 13 - Debugging dan Testing

Nama: Revalina Stefani
NIM: 2225250200
Kelas: 3B

## Kasus
Program mengolah nilai mahasiswa, menghitung rata-rata,
menentukan status kelulusan, dan mencari nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Awal | Status Awal |
|---|---|---|---|---|
| T1 | [80,60,90,70] | 75.0 | 60.0 | FAIL |
| T2 | [100,80] | 90.0 | 36.0 | FAIL |
| T3 | 60 | Lulus | Tidak lulus | FAIL |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80,60,90,70] | 90 | 0 | FAIL |

## Bug Report

### B01 - Rata-rata
Gejala: Hasil rata-rata tidak sesuai.
Akar penyebab: Pembagi selalu 5.
Perbaikan: Pembagi menggunakan panjang list.
Retest: T1 dan T2 PASS.

### B02 - Batas kelulusan
Gejala: Nilai 60 dinyatakan tidak lulus.
Akar penyebab: Menggunakan operator >.
Perbaikan: Menggunakan operator >=.
Retest: T3 dan T4 PASS.

### B03 - Nilai tertinggi
Gejala: Hasil nilai tertinggi adalah 0.
Akar penyebab: Kondisi pembanding terbalik.
Perbaikan: Menggunakan operator >.
Retest: T5 PASS.

## Retest
Semua lima test case telah dijalankan ulang.
Hasil yang diharapkan: seluruh test PASS.

## Cara Menjalankan
python praktik/praktik_4_debugging.py

## Refleksi
Tracing dan test case membantu menemukan kesalahan
dengan membandingkan hasil aktual dan hasil yang diharapkan.
Breakpoint membantu mengamati nilai variabel saat program berjalan.
