# UTS Newton-Raphson

Repository ini dibuat untuk memenuhi tugas UTS Praktikum Komputasi Numerik.  
Projek ini berfokus sama implementasi Metode Newton-Raphson untuk mencari akar dari persamaan non linear menggunakan bahasa pemrograman Python.

---

## 👥 Anggota Kelompok

Kelompok 4 – Metode Newton-Raphson:

- Teuku Fikram Al Syahbanna
- M. Ilham
- Inayah Kamila Nurman
- Faris Fudhaili
- Muhammad Azlan Syahkam

Cara Kerja Program
1. Pengguna memasukkan fungsi \( f(x) \), nilai awal \( x_0 \), toleransi error, dan jumlah iterasi maksimum.
2. Program mengubah input string menjadi persamaan matematika menggunakan `sympify()`.
3. Program menghitung turunan dari fungsi tersebut secara simbolik.
4. Iterasi dilakukan menggunakan rumus:
   \[
   x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
   \]
5. Iterasi berhenti jika:
   - Nilai \( |f(x)| \) sudah lebih kecil dari toleransi, atau  
   - Jumlah iterasi mencapai batas maksimum.
