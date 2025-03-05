def horner_synthetic(coeffs, x):
    result = coeffs[0]  # Koefisien pertama
    intermediate = [result]  # Menyimpan hasil tiap langkah

    for i in range(1, len(coeffs)):
        result = result * x + coeffs[i]
        intermediate.append(result)
    return result, intermediate
coeffs = [-1, 0, 2, 0, 3, 5]  # Koefisien polinomial: -x^5 + 2x^3 + 3x + 5
x = -2  # Nilai x yang diuji
result, steps = horner_synthetic(coeffs, x)
# Menampilkan langkah-langkah perhitungan
print(f"Evaluasi f({x}) menggunakan Horner's Rule:")
for i, step in enumerate(steps):
    print(f"Step {i}: {step}")
print(f"\nHasil akhir f({x}) = {result}")
