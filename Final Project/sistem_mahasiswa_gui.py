import tkinter
from tkinter import messagebox

class Mahasiswa:
    def __init__(self, nama, nim, usia, juruan, alamat):
        self.nama = nama
        self.nim = nim
        self.usia = usia
        self.juruan = juruan
        self.alamat = alamat
        self.tahun_masuk = "20" + nim[:2]

    def simpan_data(self):
        return {
            "Nama": self.nama,
            "NIM": self.nim,
            "Tahun Masuk": self.tahun_masuk,
            "Usia" : self.usia,
            "Juruan" : self.juruan,
            "Alamat" : self.alamat
        }