import sys,os,time


def clear():
    os.system("cls")

def typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)



def tambah():
    angka1 = int(input("Masukkan Angka 1 : "))
    angka2 = int(input("MAsukkan Angka 2 : "))
    proses = angka1 + angka2
    print("Hasil Penjumalahan :",proses)

def kurang():
    angka1 = int(input("Masukkan Angka 1 : "))
    angka2 = int(input("Masukkan Angka 2 : "))
    proses = angka1 - angka2
    print("Hasil Pengurangan :",proses)

def bagi():
    angka1 = int(input("Masukkan Angka 1 : "))
    angka2 = int(input("Masukkan Angka 2 : "))
    proses = angka1 / angka2
    print("Hasil Pembagian :",proses)

def perkalian():
    angka1 = int(input("Masukkan Angka 1 : "))
    angka2 = int(input("Masukkan Angka 2 : "))
    proses = angka1 * angka2
    print("Hasil Perkalian :",proses)

def quit():
    typing("Program selesai dan akan di clear dalam 3..")
    time.sleep(1)
    typing(" 2..")
    time.sleep(1)
    typing(" 1..")
    time.sleep(1)
    clear()
    exit()

while True:
    print("Silahkan memilih menu:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. perkalian")
    print("4. Pembagian")
    print("5. Exit")
    pilih = int(input("Masukkan Pilihan : "))
    if pilih == 1: # penjumlahan
        tambah()
        while True:
            try:
                tanya = input("Masih mau memilih (ya/tidak)? ")
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
            quit()
            break
        else:
            print("Invalid")

    elif pilih == 2: # pengurangan
        kurang()
        while True:
            try:
                tanya = input("Masih mau memilih (ya/tidak)? ")
            except ValueError:
                continue
            if tanya == 'ya' or tanya == 'Ya' or tanya == 'YA':
                break
            elif tanya == 'tidak' or tanya == 'Tidak':
                break
            else:
                print("Invalid")
                continue
        if tanya == 'ya':
            continue
        elif tanya == 'tidak':
            # quit()
            break
        else:
            print("Invalid")

    elif pilih == 3: # perkalian
        perkalian()
        while True:
            try:
                tanya = input("Masih mau memilih (ya/tidak)? ")
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
            quit()
            break
        else:
            print("Invalid")

    elif pilih == 4: # pembagian
        bagi()
        while True:
            try:
                tanya = input("Masih mau memilih (ya/tidak)? ")
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
            quit()
            break
        else:
            print("Invalid")

    elif pilih == 5: # exit
        quit()

    else:
        print("Invalid")
