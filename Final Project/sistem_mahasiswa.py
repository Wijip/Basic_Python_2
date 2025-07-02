class Mahasiswa:
    def __init__(self, nama, nim, usia, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.usia = usia
        self.jurusan = jurusan
        self.alamat = alamat
        self.tahun_masuk = "20" + nim[:2]


    def simpan_data(self):
        data = {
            "Nama": self.nama,
            "NIM": self.nim,
            "Usia": self.usia,
            "Jurusan": self.jurusan,
            "Alamat": self.alamat,
            "Tahun Masuk": self.tahun_masuk
        }
        return data

    def tampilkan_data(self):
        data = self.simpan_data()
        print("Berikut Data Mahasiswa:")
        print(f"Nama Mahasiswa   : {data['Nama']}")
        print(f"NIM Mahasiswa    : {data['NIM']}")
        print(f"Tahun Masuk      : {data['Tahun Masuk']}")
        print(f"Usia Mahasiswa   : {data['Usia']}")
        print(f"Jurusan Mahasiswa: {data['Jurusan']}")
        print(f"Alamat Mahasiswa : {data['Alamat']}")
        print("Terimakasih Sudah Menggunakan Sistem Ini")

nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
usia = input("Masukkan Usia: ")
jurusan = input("Masukkan Jurusan: ")
alamat = input("Masukkan Alamat: ")

mahasiswa_baru = Mahasiswa(nama, nim, usia, jurusan, alamat)
mahasiswa_baru.tampilkan_data()