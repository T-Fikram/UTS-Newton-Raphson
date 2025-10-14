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
        print("\nTerima kasih, sampai berjumpa kembali👋")
        sys.exit(0)

    elif pilihan == "1":
        # Masuk langsung ke loop tanpa kembali ke menu lagi
        while True:
            try:
                # ======================== INPUT DARI PENGGUNA ========================
                print("\nJika operasi adalah sebuah perkalian gunakan tanda *")
                print("Contoh: x^2 - 4*x + 4")

                fungsi_input = str(input("\nMasukkan fungsi f(x): "))
                x = float(input("Masukkan nilai x (tebakan awal): "))
                toleransi_error = float(input("Masukkan toleransi: "))
                n = int(input("Masukkan iterasi maksimum: "))

                print("\nMemproses...\n")
                time.sleep(1)

                x_simbol = symbols('x')

                def parse(persamaan):
                    persamaan = persamaan.lower().replace(" ", "")
                    persamaan = persamaan.replace("akar(", "sqrt(")
                    persamaan = persamaan.replace("^", "**")
                    return sympify(persamaan)

                fungsi = parse(fungsi_input)

                def f(x):
                    return fungsi.subs(x_simbol, x).evalf()

                def turunan(x):
                    return diff(fungsi, x_simbol).subs(x_simbol, x).evalf()

            except Exception:
                print("\n❌ Fungsi tidak valid! Contoh yang benar: x^2 - 4*x + 4")
                continue

            # ======================== TABEL OUTPUT ITERASI ========================
            print("=" * 90)
            print("| {:<8} | {:<12} | {:<15} | {:<15} | {:<15} |".format("Iterasi", "x", "f(x)", "f'(x)", "Δx"))
            print("=" * 90)

            konvergen = False
            i = 1

            while i <= n:
                fx = f(x)
                dfx = turunan(x)

                if abs(fx) < toleransi_error:
                    konvergen = True
                    break

                if dfx == 0:
                    print("Turunan nol! Tidak bisa lanjut iterasi.")
                    sys.exit(1)

                x_new = x - fx / dfx
                delta_x = abs(x_new - x)

                print("| {:<8} | {:<12.6f} | {:<15.6f} | {:<15.6f} | {:<15.6f} |".format(
                    i, x_new, f(x_new), turunan(x_new), delta_x))

                x = x_new
                i += 1

            print("=" * 90)

            if konvergen:
                print(f"\n✅ Konvergen! Akar yang ditemukan adalah {x} pada iterasi ke-{i-1}")
            else:
                print(f"\n ⚠️ Metode berhenti pada iterasi ke-{n} karena mencapai batas iterasi maksimum.")
                print("❌ Solusi belum konvergen.")

            print("=" * 60)
            print("Program selesai dijalankan.")
            print("=" * 60)

            # Opsi ulang -- TANPA kembali ke menu
            ulang = input("\nApakah ingin mencoba lagi dengan fungsi lain? (y/n): ").lower()
            if ulang != "y":
                print("\nTerima kasih telah menggunakan program ini👋")
                sys.exit(0)

            print("\nMengulang program...\n")
            time.sleep(1)

    else:
        print("\n⚠️  Pilihan tidak valid. Masukkan angka 1 atau 2.")
