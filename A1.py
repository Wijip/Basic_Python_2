def jumlah(*data):
    total = sum(data)
    avg = total / 10
    return total, avg

data = []
for i in range(10):
    data.append(int(input("Masukkan angka: ")))
total_angka = jumlah(*data)
print("Total: ", total_angka)
rata_rata = (lambda total, length: total/length)(total_angka, len(data))
print("Rata-rata: ", rata_rata)