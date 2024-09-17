# Aplikasi Bisokop

Aplikasi ini memungkinkan Anda mengelola menu pembayaran pada bioskop sebagai kasir.

## Petunjuk Penggunaan

### Persyaratan

- Python (versi 3.x)
- Library mysql-connector-python
- Library PyQt5
- Library bcrypt

### Akun Untuk Login

```
    Email   : kasir
    Password: 12345
```

### Instalasi

1. Unduh atau salin seluruh isi repositori ini.
2. Buka terminal/command prompt.
3. Navigasikan ke direktori tempat Anda menyimpan aplikasi.
4. Import data tabel bioskop.sql dan login.sql ke database mysql Anda.
5. Di file DB.py konfigurasikan database sesuai dengan database Anda.
6. Install library yang diperlukan apabila sebelum nya belum menginstalnya
7. Jalankan file FrmLogin.py untuk menjalankan aplikasi.

### Penggunaan Aplikasi

1. Setelah menjalankan aplikasi, Masukkan username "kasir" dan password "12345" lalu klik tombol submit untuk melanjutkan, lalu klik ok pada warning text, log in berhasil.
2. Setelah Login kemudian klik tombol Kasir untuk melanjutkan ke dalam FrmBioskop.py.
3. Masukkan informasi pemesanan (tidak dapat memasukkan nomor kursi yang sama apabila kursi telah dipesan)
4. Klik tombol "Simpan" untuk menyimpan data pemesanan kursi.
5. Pada kolom treeview untuk melihat data pemesanan yang sudah dimasukkan.

### Pengembang

Aplikasi ini dikembangkan oleh [Nur Iskandar S, 220511009, TI22L]
