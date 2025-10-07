# Metode Newton-Raphson ditulis di sini

import sys
from sympy import diff, sympify, symbols
import time

# Tampilan awal program
print("=" * 60)
print("          PROGRAM METODE NEWTON-RAPHSON")
print("=" * 60)


# Kondisi pilihan pengguna
while True:
    print("\n[1] Masuk ke program")
    print("[2] Keluar")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "2":
        print("\nTerima kasih telah menggunakan Harrit Solver. 👋")
        sys.exit(0)

    

    elif pilihan == "1":
        # Input dari pengguna

        print("\nJika operasi adalah sebuah perkalian gunakan tanda *")
        print("Contoh: x^2 - 4*x + 4")

        fungsi_input = str(input("\nMasukkan fungsi f(x): "))
        x = int(input("Masukkan nilai x: "))
        toleransi_error = float(input("Masukkan toleransi: "))
        n = int(input("Masukkan iterasi maksimum: "))

        print("\nMemproses...\n")
        time.sleep(1)  # jeda agar terasa interaktif

        # Mendefinisikan simbol x untuk digunakan di Sympy
        x_simbol = symbols('x')

        # Fungsi untuk mengubah string input menjadi persamaan matematika Sympy
        def parse(persamaan):
            persamaan = persamaan.lower().replace(" ", "") # hilangkan spasi
            persamaan = persamaan.replace("akar(", "sqrt(") # ubah "akar" jadi "sqrt"
            persamaan = persamaan.replace("^", "**") # ubah ^ jadi **
            return sympify(persamaan) # ubah string jadi persamaan Sympy

        # Parse fungsi dari input
        fungsi = parse(fungsi_input)

        # Definisi fungsi f(x)
        def f(x):
            return fungsi.subs(x_simbol, x).evalf() # substitusi nilai x dan evaluasi hasilnya

        # Definisi turunan f'(x)
        def turunan(x):
            return diff(fungsi, x_simbol).subs(x_simbol, x).evalf() # turunan dan substitusi nilai x

        # Header tabel
        print("=" * 70)
        print("| {:<8} | {:<12} | {:<15} | {:<15} |".format("Iterasi", "x", "f(x)", "f'(x)"))
        print("=" * 70)

        # Proses iterasi metode Newton-Raphson
        i = 1
        while i < n and abs(f(x)) >= toleransi_error:
            if turunan(x) == 0:
                print("Turunan nol! Tidak bisa lanjut iterasi.")
                sys.exit(1) # keluar program jika f'(x) = 0

            x = x - f(x)/turunan(x)

            # Cetak hasil iterasi dalam bentuk tabel
            print("| {:<8} | {:<12.6f} | {:<15.6f} | {:<15.6f} |".format(i, x, f(x), turunan(x)))

            # Rumus Newton-Raphson
            i += 1

        # Cetak hasil akhir
        print("=" * 70)
        print("| {:<8} | {:<12.6f} | {:<15.6f} | {:<15.6f} |".format(i, x, f(x), turunan(x)))
        print("=" * 70)

        # Cek hasil konvergensi
        if abs(f(x)) >= toleransi_error:
            print(f"\n❌ Tidak konvergen! Akar adalah {x} pada iterasi ke-{i}")
        else:
            print(f"\n✅ Konvergen! Akar yang ditemukan adalah {x} pada iterasi ke-{i}")

        print("=" * 60)
        print("Program selesai dijalankan.")
        print("=" * 60)

        # Tanya apakah ingin mengulang
        ulang = input("\nApakah ingin menjalankan lagi? (y/n): ").lower()
        if ulang != "y":
            print("\nTerima kasih telah menggunakan Harrit Solver. 👋")
            sys.exit(0)
        else:
            print("\nMengulang program...\n")
            time.sleep(1)
    else:
        print("\n⚠️  Pilihan tidak valid. Masukkan angka 1 atau 2.")
