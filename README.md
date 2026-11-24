# Sistem Rental Kendaraan

Project konsol sederhana untuk mengelola penyewaan dan pengembalian kendaraan. Dibuat dengan Python tanpa dependensi tambahan.

## Menjalankan aplikasi

```bash
python main.py
```

Pilih menu untuk melihat kendaraan, menyewa kendaraan berdasarkan nomor dan durasi, atau mengembalikannya. Data kendaraan contoh dimuat setiap kali program dijalankan.

## Konsep OOP yang digunakan

- **Class dan objek:** `Kendaraan` dan `SistemRental`; sistem contoh membuat beberapa objek `Kendaraan`.
- **Constructor:** `__init__()` menginisialisasi data kendaraan dan sistem rental.
- **Attribute dan method:** kendaraan menyimpan nama, jenis, tarif, dan status; method mengelola penyewaan/pengembalian.
- **Encapsulation:** attribute internal menggunakan awalan `__` dan status ketersediaan hanya diubah melalui method.
- **Property dan setter:** property `tarif_per_hari` memvalidasi tarif sebelum disimpan.
- **Class method:** `SistemRental.dengan_data_contoh()` membuat sistem yang berisi kendaraan contoh.
- **Static method:** `Kendaraan.validasi_durasi()` memvalidasi lama sewa dan `SistemRental.hitung_total()` menghitung biaya.
