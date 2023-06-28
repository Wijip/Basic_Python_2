# Fungsi dan parameter

def function1(name): # Nama
    print(f'halo {name} welcome to koding akademi')
function1('wiji')
print()
def function2(panjang, lebar): #luas persegi panjang
    luas = panjang * lebar
    print(f'Luas persegi panjang = {luas}')
function2(10,12)


# fungsi yang mengembalikan nilai
def function3(panjang, lebar): # luas persegi panjang
    luas = panjang * lebar
    return luas

l = function3(10, 12)
print(f'Luas persegi panjang = {l}')

# pemanggilan function dari function lain
def function4(sisi): # luas persegi
    luas = sisi * sisi
    return luas
def function5(sisi):
    volume = function4(sisi)*sisi
    return volume
print()
print(f'Luas persegi panjang sisi 10 = {function4(10)}')
print(f'Volume persegi panjang sisi 10 = {function5(10)}')

# function yang dapat memanggil dirinya sendiri
print()
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

nilai_faktorial = faktorial(5)
print(f"nilai factorial = {nilai_faktorial}")