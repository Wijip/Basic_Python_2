with open('data_angka.txt', 'r') as f:
    data = f.readlines()

genap = 0
ganjil = 0

for line in data:
    num = int(line.strip())
    print(num)
    if num % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print(f'Jumlah Bilangan Genap  : {genap}')
print(f'Jumlah Bilangan Ganjil : {ganjil}')