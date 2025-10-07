# Metode Newton-Raphson ditulis di sini

import sys
from sympy import diff, sympify, symbols

# Input dari pengguna
fungsi_input = str(input("Masukkan fungsi f(x): "))
x = int(input("Masukkan nilai x: "))
toleransi_error = float(input("Masukkan toleransi: "))
n = int(input("Masukkan iterasi maksimum: "))

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

# Proses iterasi metode Newton-Raphson
i = 1
while i < n and abs(f(x)) >= toleransi_error:
    if turunan(x) == 0:
        print("Turunan nol! Tidak bisa lanjut iterasi.")
        sys.exit(1) # keluar program jika f'(x) = 0

    # Rumus Newton-Raphson
    x = x - f(x)/turunan(x)
    i += 1

# Cek hasil konvergensi
if abs(f(x)) >= toleransi_error:
    print(f"\nTidak konvergen! Akar adalah {x} pada iterasi {i}")
else:
    print(f"\nKonvergen! Akar yang ditemukan adalah {x} pada iterasi {i}")
