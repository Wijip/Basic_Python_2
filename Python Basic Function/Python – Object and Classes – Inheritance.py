class Manusia:
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat

    def perkenalan(self):
        print(f'Halo, Nama saya {self.nama} dengan tinggi {self.tinggi} cm dan berat {self.berat} Kg')

robert = Manusia("robert", 175, 68)
robert.perkenalan()

# class Pekerja(Manusia):
#     pass
#
# class Pelajar(Manusia):
#     pass
#
# class Pengusaha(Manusia):
#     pass
#
# clara = Pekerja("Clara", 160, 46)
# clara.perkenalan()
#
# diana = Pelajar("Diana", 156, 42)
# diana.perkenalan()
#
# robi = Pengusaha("Robi", 172, 66)
# robi.perkenalan()

class Pekerja(Manusia):
    def __init__(self, nama, tinggi, berat, pekerjaan, tahun_kerja):
        super().__init__(nama, tinggi, berat)
        self.pekerjaan = pekerjaan
        self.tahun_kerja = tahun_kerja

    def perkenalan(self):
        print(f'Halo , nama saya {self.nama} dengan tinggi {self.tinggi} cm dan berat {self.berat} Kg dan bekerja sebagai {self.pekerjaan}dan sudah bekerja selama {self.tahun_kerja}')

# class Pelajar(Manusia):
#     def __init__(self, nama, tinggi, berat, sekolah):
#         Manusia.__init__(self, nama, tinggi, berat)
#         self.sekolah = sekolah
#
#     def perkenalan(self):
#         print(f'Halo, nama saya {self.nama} dengan tinggi {self.tinggi} cm dan berat {self.berat} kg dan saya siswa dari sekolah {self.sekolah}')

clara = Pekerja("Clara", 160, 45, "Dokter", 10)
clara.perkenalan()

# diana = Pelajar("Diana", 156, 42, "SMP Negeri 1 Surabaya")
# diana.perkenalan()