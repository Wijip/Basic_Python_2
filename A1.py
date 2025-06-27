class Manusia:
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat
    def perkenalan(self):
        print("Halo, nama saya ", self.nama, "dengan tinggi ", self.tinggi, "cm dan berat ", self.berat, "kg")

robert = Manusia("Robert", 175, 68)
robert.perkenalan()