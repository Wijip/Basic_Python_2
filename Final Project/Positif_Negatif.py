negatif_num = []
positif_num = []

for i in range(10):
    number1 = int(input(f"masukkan angka ke {i+1}: "))
    if number1 > 0:
        positif_num.append(number1)
    else:
        negatif_num.append(number1)

print(f"Bilangan Positif : {positif_num}")
print(f"Bilangan Negatif : {negatif_num}")