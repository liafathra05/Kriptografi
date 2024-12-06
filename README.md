# Kriptografi

# Program Enkripsi dan Dekripsi
Program ini adalah aplikasi Python untuk enkripsi dan dekripsi menggunakan tiga algoritma kriptografi: Vigenere Cipher, Playfair Cipher, dan Hill Cipher. Program ini memiliki antarmuka pengguna grafis (GUI) yang dibuat dengan tkinter dan dapat menerima input teks melalui keyboard atau file.

# Cara Menjalankan Program
1. Persiapan Lingkungan
- Pastikan Python 3.x sudah terinstal di komputer.
- Instal numpy jika belum terinstal dengan perintah: pip install numpy

2. Struktur File
- vigenere_cipher.py: Berisi implementasi algoritma Vigenere Cipher.
- playfair_cipher.py: Berisi implementasi algoritma Playfair Cipher.
- hill_cipher.py: Berisi implementasi algoritma Hill Cipher.
- main.py: Program utama berbasis teks yang memungkinkan pengguna memilih algoritma cipher dan melakukan enkripsi atau dekripsi.
- gui.py: Berisi kode untuk antarmuka pengguna grafis (GUI) untuk program.

3. Menjalankan Program
- Buka terminal atau command prompt.
- Navigasikan ke direktori tempat file gui.py disimpan.
- Jalankan program dengan perintah: gui.py

4. Menggunakan Program
- Input Teks: Ketikkan teks secara langsung ke dalam antarmuka atau mengunggah file teks dengan tombol "Upload File".
- Memilih Cipher: Pilih algoritma cipher (Vigenere, Playfair, atau Hill) dari menu dropdown.
- Memasukkan Kunci: Masukkan kunci yang diperlukan (panjang kunci minimal 12 karakter).
- Enkripsi/Dekripsi: Klik tombol "Enkripsi" atau "Dekripsi" untuk memproses teks.
- Menyimpan Output: Gunakan tombol "Simpan Output" untuk menyimpan hasil ke dalam file teks.
