# class Kucing:
#     jumlah_kaki = 4
#     jumlah_ekor = 1
#     warna = None
#
#     def makan(self):
#         print("Kucing Makan")
#
#     def mengeong(self):
#         print("Kucing Mengeong")
#
#     def berjalan(self):
#         print("Kucing Berjalan")
#
# anggora = Kucing()
# persia = Kucing()
# sphynx = Kucing()
#
# print(f'jumlah kaki = {anggora.jumlah_kaki}')
# print(f'Jumlah Ekor = {anggora.jumlah_ekor}')
# print(f'Kucing makan = {anggora.makan()}')
# print(f'Kucing mengeong = {anggora.mengeong()}')
# print(f'Kucing berjalan = {anggora.berjalan()}')

class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def greetings(self):
        print("Halo, perkenalkan nama saya ", self.nama)
        print("Usia saya adalah ", self.umur )

robert = Mahasiswa("robert", 14)
robert.greetings()