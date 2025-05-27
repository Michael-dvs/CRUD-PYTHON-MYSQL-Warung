# CRUD Python-MySQL Warung

Aplikasi CRUD (Create, Read, Update, Delete) berbasis GUI menggunakan Python (Tkinter) dan MySQL untuk manajemen data barang di warung/toko sederhana.

## Fitur
- **Create**: Tambah data barang baru ke database.
- **Read**: Cari dan tampilkan data barang beserta stok dan harga.
- **Update**: Ubah data barang yang sudah ada.
- **Delete**: Hapus data barang dari database.
- **Dashboard**: Tampilkan ringkasan jumlah barang dan stok.

## Teknologi
- Python 3
- Tkinter (GUI)
- PyMySQL (koneksi ke MySQL)
- MySQL (database)

## Cara Menjalankan
1. Pastikan MySQL sudah terinstall dan database sudah dibuat sesuai konfigurasi di kode.
2. Install dependensi Python:
   ```bash
   pip install pymysql
   ```
3. Jalankan aplikasi:
   ```bash
   python main.py
   ```

## Struktur Folder
- `build/` : Berisi file Python untuk setiap fitur (Create, Read, Update, Delete, Home) dan aset gambar.
- `assets/` : Berisi gambar-gambar tombol dan elemen UI.

## Catatan
- Ubah konfigurasi database (user, password, nama database) di setiap file Python sesuai dengan setup MySQL Anda.
- Aplikasi ini cocok untuk pembelajaran CRUD dan pengelolaan data sederhana di toko/warung.

---

Dibuat oleh Michael-dvs
