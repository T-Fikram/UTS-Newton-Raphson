# Metode Newton-Raphson ditulis di sini

import sys
from sympy import diff, sympify, symbols

fungsi_input = str(input("Masukkan fungsi f(x): "))
x = int(input("Masukkan nilai x: "))
toleransi_error = float(input("Masukkan toleransi: "))
n = int(input("Masukkan iterasi maksimum: "))

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


i = 1
while i < n and abs(f(x)) >= toleransi_error:
    if turunan(x) == 0:
        print("Turunan nol! Tidak bisa lanjut iterasi.")
        sys.exit(1)

    x = x - f(x)/turunan(x)
    i += 1

if abs(f(x)) >= toleransi_error:
    print(f"\nTidak konvergen! Akar adalah {x} pada iterasi {i}")
else:
    print(f"\nKonvergen! Akar yang ditemukan adalah {x} pada iterasi {i}")
