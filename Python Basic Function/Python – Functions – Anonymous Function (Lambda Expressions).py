greeting = lambda name : print(f'Hello {name} Welcome to koding akademi')
greeting('nama1')
greeting('nama2')
greeting('nama3')



# *args * kwargs
print()
def greeting(*args):
    for name in args:
        print("Halo ", name)

greeting("John","Robert","Sisca")

print()
list_nomer = [123, 888, 4444]
isi_sms = {'tujuan': 4444, 'pesan': 'mau daftar pak'}
def kirim(*list_nomor):
    print(list_nomor)

def tulis(**isi):
    print(isi)

kirim(123,838,4939)

tulis(tujuan=123, pesan='apa kabar')

# pemanggilan fungsi
kirim(*list_nomer)
tulis(**isi_sms)

#fungsi rata rata
print()
def rata_rata(*data):
    banyak_data = len(data)
    jumlah_data = sum(data)
    nilai_rata_rata = float(jumlah_data) / float(banyak_data)
    return nilai_rata_rata

print(rata_rata(2,4,1,2,4,1,2,3,4,5,1,8,2))