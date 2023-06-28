def group_number():
    positive_numbers = []
    negative_numbers = []
    for i in range(10):
        i += 1
        num = int(input(f'Masukkan Angka ke-{i} : '))
        if num > 0:
            positive_numbers.append(num)
        else:
            negative_numbers.append(num)

    return positive_numbers, negative_numbers

positif, negatif = group_number()

print(f'Bilangan Posifit : {positif}')
print(f'Bilangan Negatif : {negatif}')