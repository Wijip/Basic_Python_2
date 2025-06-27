class Mahasiswa:
    def __init__(self, nama, nim, usia, jurusan, alamat):
        """Inisialisasi data mahasiswa."""
        self.nama = nama
        self.nim = nim
        self.usia = usia
        self.jurusan = jurusan
        self.alamat = alamat
        # Ambil dua digit pertama dari NIM untuk tahun masuk
        self.tahun_masuk = "20" + nim[:3]  # Format seperti 2017, 2018, dsb.

    def simpan_data(self):
        """Simpan data mahasiswa ke dalam dictionary."""
        data = {
            "Nama": self.nama,
            "NIM": self.nim,
            "Usia": self.usia,
            "Jurusan": self.jurusan,
            "Alamat": self.alamat,
            "Tahun Masuk": self.tahun_masuk
        }
        return data
    #1741720036
    #17 41 72 00 36

    def tampilkan_data(self):
        """Tampilkan data mahasiswa yang sudah tersimpan."""
        data = self.simpan_data()
        print("Berikut Data Mahasiswa:")
        print(f"Nama Mahasiswa   : {data['Nama']}")
        print(f"NIM Mahasiswa    : {data['NIM']}")
        print(f"Tahun Masuk      : {data['Tahun Masuk']}")
        print(f"Usia Mahasiswa   : {data['Usia']}")
        print(f"Jurusan Mahasiswa: {data['Jurusan']}")
        print(f"Alamat Mahasiswa : {data['Alamat']}")
        print("Terimakasih Sudah Menggunakan Sistem Ini")


# Input data mahasiswa dari pengguna
nama = input("Masukan Nama: ")
nim = input("Masukan NIM: ")
usia = input("Masukan Usia: ")
jurusan = input("Masukan Jurusan: ")
alamat = input("Masukan Alamat: ")

# Membuat objek Mahasiswa dengan data yang diinputkan
mahasiswa_baru = Mahasiswa(nama, nim, usia, jurusan, alamat)

# Menampilkan data mahasiswa
mahasiswa_baru.tampilkan_data()
