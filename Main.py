# ======================== METODE NEWTON-RAPHSON ========================

import sys
from sympy import diff, sympify, symbols
import time

# ======================== TAMPILAN AWAL PROGRAM ========================
print("=" * 60)
print("          PROGRAM METODE NEWTON-RAPHSON")
print("=" * 60)

# ======================== MENU UTAMA PROGRAM ===========================
while True:
    print("\n[1] Masuk ke program")
    print("[2] Keluar")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "2":  
        # Jika memilih keluar
        print("\nTerima kasih, sampai berjumpa kembali👋")
        sys.exit(0)

    elif pilihan == "1":
        try:
            # ======================== INPUT DARI PENGGUNA ========================
            print("\nJika operasi adalah sebuah perkalian gunakan tanda *")
            print("Contoh: x^2 - 4*x + 4")

            fungsi_input = str(input("\nMasukkan fungsi f(x): "))      # Input fungsi
            x = float(input("Masukkan nilai x (tebakan awal): "))      # Tebakan awal
            toleransi_error = float(input("Masukkan toleransi: "))     # Batas error
            n = int(input("Masukkan iterasi maksimum: "))              # Iterasi maksimum

            print("\nMemproses...\n")
            time.sleep(1)

            x_simbol = symbols('x')

            # Fungsi PARSE untuk memproses input agar bisa diterima oleh SymPy
            def parse(persamaan):
                persamaan = persamaan.lower().replace(" ", "")
                persamaan = persamaan.replace("akar(", "sqrt(")
                persamaan = persamaan.replace("^", "**")
                return sympify(persamaan)

            fungsi = parse(fungsi_input)

            # Definisi fungsi f(x) dan turunannya f'(x)
            def f(x):
                return fungsi.subs(x_simbol, x).evalf()

            def turunan(x):
                return diff(fungsi, x_simbol).subs(x_simbol, x).evalf()

        except Exception:
            # Jika input fungsi salah
            print("\n❌ Fungsi tidak valid! Contoh yang benar: x^2 - 4*x + 4")
            continue

        # ======================== TABEL OUTPUT ITERASI ========================
        print("=" * 90)
        print("| {:<8} | {:<12} | {:<15} | {:<15} | {:<15} |".format("Iterasi", "x", "f(x)", "f'(x)", "Δx"))
        print("=" * 90)

        konvergen = False  # Flag untuk mengecek apakah berhasil atau tidak
        i = 1

        # ======================== PROSES ITERASI NEWTON-RAPHSON ========================
        while i <= n:
            fx = f(x)
            dfx = turunan(x)

            # Cek konvergensi berdasarkan f(x)
            if abs(fx) < toleransi_error:
                konvergen = True
                break  # Sudah konvergen, langsung keluar

            # Jika turunan nol → tidak bisa dilanjutkan
            if dfx == 0:
                print("Turunan nol! Tidak bisa lanjut iterasi.")
                sys.exit(1)

            # Rumus Newton-Raphson : x_new = x - f(x)/f'(x)
            x_new = x - fx / dfx
            delta_x = abs(x_new - x)

            # Cetak hasil iterasi
            print("| {:<8} | {:<12.6f} | {:<15.6f} | {:<15.6f} | {:<15.6f} |".format(
                i, x_new, f(x_new), turunan(x_new), delta_x))

            x = x_new
            i += 1

        print("=" * 90)

        # ======================== HASIL AKHIR ========================
        if konvergen:
            print(f"\n✅ Konvergen! Akar yang ditemukan adalah {x} pada iterasi ke-{i-1}")
        else:
            print(f"\n ⚠️ Metode berhenti pada iterasi ke-{n} karena mencapai batas iterasi maksimum.")
            print("❌ Solusi belum konvergen.")

        print("=" * 60)
        print("Program selesai dijalankan.")
        print("=" * 60)

        # ======================== OPSI ULANG PROGRAM ========================
        ulang = input("\nApakah ingin menjalankan lagi? (y/n): ").lower()
        if ulang != "y":
            print("\nTerima kasih telah menggunakan program ini👋")
            sys.exit(0)
        else:
            print("\nMengulang program...\n")
            time.sleep(1)

    else:
        print("\n⚠️  Pilihan tidak valid. Masukkan angka 1 atau 2.")
