def hitung_pendapatan(g, j):
    k = j * 5  
    p = g * k
    pa = 0.14 * p
    ps = p - pa
    bba = 0.10 * ps
    bat = 0.01 * ps
    sub = ps - bba - bat
    s = 0.25 * sub
    say = 0.30 * s
    sd = 0.70 * s
    return (p, ps, bba, bat, s, say, sd)

g = float(input("Masukkan gaji per jam yang Anda inginkan: "))
j = int(input("Masukkan jumlah jam kerja per minggu: "))

p, ps, bba, bat, s, say, sd = hitung_pendapatan(g, j)

print(f"1. Pendapatan Budi sebelum pajak: Rp {p}")
print(f"2. Pendapatan Budi setelah pajak: Rp {ps}")
print(f"3. Belanja baju dan aksesoris: Rp {bba}")
print(f"4. Belanja alat tulis: Rp {bat}")
print(f"5. Sedekah: Rp {s}")
print(f"6. Sedekah untuk anak yatim: Rp {say}")
print(f"7. Sedekah untuk kaum dhuafa: Rp {sd}")