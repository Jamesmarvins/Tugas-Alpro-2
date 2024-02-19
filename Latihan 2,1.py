def hitung_berat_badan(tinggi_badan, bmi_harap):
    berat_badan = bmi_harap * (tinggi_badan**2)
    return berat_badan

tinggi_badan = float(input("Masukkan tinggi badan (dalam meter): "))
bmi_harap = float(input("Masukkan nilai BMI yang diharapkan: "))

berat_badan_diperlukan = hitung_berat_badan(tinggi_badan, bmi_harap)
print(f"Berat badan yang diperlukan untuk tinggi badan {tinggi_badan} m dan BMI {bmi_harap} adalah {berat_badan_diperlukan:.2f} kg")