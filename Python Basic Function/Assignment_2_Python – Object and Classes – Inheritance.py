class Manusia:
    def __init__(self, nama, umur, tinggi, berat):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.berat = berat

    def detail(self):
        print(f'Halo, nama saya {self.nama}, umur saya {self.umur} tahun. saya memiliki tinggi {self.tinggi} cm dan berat {self.berat} kg.')

class Customer(Manusia):
    def __init__(self, nama, umur, tinggi, berat, customerID, store):
        Manusia.__init__(self, nama, umur, tinggi, berat)
        self.custimerID = customerID
        self.store = store

    def detail(self):
        print(f'Halo, nama saya {self.nama}, umur saya {self.umur} tahun. saya memiliki tinggi {self.tinggi} cm dan berat {self.berat} kg. saya adalah pelanggan dari toko {self.store} dengan memilikin nomor pelanggan : {self.custimerID}')

class Employee(Manusia):
    def __init__(self, nama, umur, tinggi, berat, employeeID, position, company):
        Manusia.__init__(self, nama, umur, tinggi, berat)
        self.employeeID = employeeID
        self.position = position
        self.company = company

    def detail(self):
        print(f'Halo, nama saya {self.nama}, umur saya {self.umur} tahun. saya memiliki tinggi {self.tinggi} cm dan berat {self.berat} kg. saya bekerja di perusahaan {self.company} sabagai {self.position}. Employee ID : {self.employeeID}')

class Manager(Employee):
    pass

class Developer(Employee):
    pass

clara = Customer("Clara", 20, 160, 45, 990001, "Company Store A")
clara.detail()

rio = Manager("Rio", 32, 174, 64, 2121001, "Manager", "Company A")
rio.detail()

ciko = Developer("Ciko", 24, 180, 75, 2122001, "Developer", "Company A")
ciko.detail()

