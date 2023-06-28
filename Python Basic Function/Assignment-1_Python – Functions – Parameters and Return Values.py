import time


def tambah(a,b):
    penjumlahan = a + b
    return penjumlahan

def kurang(a,b):
    pengurangan = a - b
    return pengurangan

def bagi(a,b):
    pembagian = a / b
    return pembagian

def kali(a,b):
    perkalian = a * b
    return perkalian

while True:
    print("Silahkan memilih Menu:")
    print("1. Penjumalhan")
    print("2. Pengurangan")
    print("3. Pembagian")
    print("4. Perkalian")
    print("5. exit")
    pilih = int(input("Masukkan pilihan anda : "))
    if pilih == 1: # penambahan
        angka1 = int(input("Masukkan Angka 1 : "))
        angka2 = int(input("Masukkan Angka 2 : "))
        # proses = tambah(angka1, angka2)
        # print(f'hasil penambahan = {proses}')
        print(f'hasil penambahan {angka1} + {angka2} = {tambah(angka1, angka2)}')
        while True:
            try:
                tanya = input("Masih mau memilih (ya/tidak)? : ")
            except ValueError:
                continue

            if tanya == 'ya':
                break
            elif tanya == 'tidak':
                break
            else:
                print("invalid")
                continue
        if tanya == 'ya':
            continue
        elif tanya == 'tidak':
            break
        else:
            print("invliad")

    elif pilih == 2: # pengurangan
        angka1 = int(input("Masukkan angka 1 : "))
        angka2 = int(input("Masukkan Angak 2 : "))
        print(f'Hasil pengurangan {angka1} - {angka2} = {kurang(angka1, angka2)}')
        while True:
            try:
                tanya = input("Masih mau memilih (ya/tidak)? : ")
            except ValueError:
                continue
            if tanya == 'ya':
                break
            elif tanya == 'tidak':
                break
            else:
                print("invliad")

        if tanya == 'ya':
            continue
        elif tanya == 'tidak':
            break
        else:
            print('Invalid')

    elif pilih == 3: #pembagian
        angka1 = int(input("Masukkan angka 1 : "))
        angka2 = int(input("Masukkan angka 2 : "))
        print(f'Hasil pembagian {angka1} : {angka2} = {bagi(angka1,angka2)}')
        while True:
            try:
                tanya = input("Masih mau memilih (ya/tidak)? : ")
            except ValueError:
                continue
            if tanya == 'ya':
                break
            elif tanya == 'tidak':
                break
            else:
                print("Invalid")
                continue
        if tanya == 'ya':
            continue
        elif tanya == 'tidak':
            break
        else:
            print("Invliad")

    elif pilih == 4: # Perkalian
        angka1 = int(input("Masukkan angka 1 : "))
        angka2 = int(input("Masukkan angka 2 : "))
        print(f'Haisl perkalian {angka1} X {angka2} = {kali(angka1,angka2)}')
        while True:
            try:
                tanya = input("Masih mau memilih (ya/tidak)? : ")
            except ValueError:
                continue
            if tanya == 'ya':
                break
            elif tanya == 'tidak':
                break
            else:
                continue
        if tanya == 'ya':
            continue
        elif tanya == 'tidak':
            break
        else:
            print("invalid")

    elif pilih == 5:
        print("bye")
        time.sleep(1)
        exit()
    else:
        print("Invalid")