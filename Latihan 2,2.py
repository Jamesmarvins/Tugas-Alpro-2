def hitung_fungsi(x):
    return (2 * x**3 + 2 * x + 15) / x

try:
    x = int(input("Masukkan bilangan bulat x: "))
    hasil = hitung_fungsi(x)
    print(f"Hasil fungsi f({x}) adalah: {hasil}")
except ValueError:
    print("Input yang dimasukkan bukan bilangan bulat.")
except ZeroDivisionError:
    print("Input yang dimasukkan tidak boleh nol.")