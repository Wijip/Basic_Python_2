class Manusia:
    def __init__(self, nama, umur, tinggi, berat):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.berat = berat

    def perkenalan(self):
        print(f'Halo, perkenalkan nama saya {self.nama} umur saya {self.umur} tahun. saya memiliki tinggi {self.tinggi} cm dan berat {self.berat} Kg')

class Person(Manusia):
    pass

class Employee(Manusia):
    def __init__(self, nama, umur, tinggi, berat, pekerjaan, employeeID):
        Manusia.__init__(self, nama, umur, tinggi, berat)
        self.pekerjaan = pekerjaan
        self.employeeID = employeeID

    def perkenalan(self):
        print(f'Halo, Nama saya {self.nama}, umur saya {self.umur} tahun. saya memiliki tinggi {self.tinggi} cm dan berat {self.berat} Kg. Saya bekerja sebagai {self.pekerjaan} dan memiliki ID kerja {self.employeeID}')

alice = Person("Alice", 18, 162, 46,)
alice.perkenalan()

ciko = Employee("Ciko", 32, 180, 72, "Dokter", 23001)
ciko.perkenalan()