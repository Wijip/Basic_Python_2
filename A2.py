def jumlah(*angka):
    total = sum(angka)
    return total

angka = []
for i in range(10):
    angka.append(int(input(f"Masukkan angka ke {i + 1}: ")))
total_angka = jumlah(*angka)
print("Total: ", total_angka)
rata_rata = (lambda total, length: total/length)(total_angka, len(angka))
print("Rata-rata: ", rata_rata)