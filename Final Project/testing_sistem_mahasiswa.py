class Mahasiswa:
    def __init__(self, nama, nim, usia, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.usia = usia
        self.jurusan = jurusan
        self.alamat = alamat
        self.tahun_masuk = "20" + nim[:2]