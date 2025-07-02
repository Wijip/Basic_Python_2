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

def tambah_mahasiswa(daftar_mahasiswa):
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    usia = input("Masukkan Usia: ")
    jurusan = input("Masukkan Jurusan: ")
    alamat = input("Masukkan Alamat: ")
    mahasiswa_baru = Mahasiswa(nama, nim, usia, jurusan, alamat)
    daftar_mahasiswa.append(mahasiswa_baru)
    print("Mahasiswa berhasil ditambahkan!")

def edit_mahasiswa(daftar_mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa.nim == nim:
            mahasiswa.nama = input("Masukkan Nama baru: ")
            mahasiswa.usia = input("Masukkan Usia baru: ")
            mahasiswa.jurusan = input("Masukkan Jurusan baru: ")
            mahasiswa.alamat = input("Masukkan Alamat baru: ")
            print("Data mahasiswa berhasil diubah!")
            return
    print("Mahasiswa tidak ditemukan!")

def lihat_data(daftar_mahasiswa):
    for mahasiswa in daftar_mahasiswa:
        mahasiswa.tampilkan_data()

def hapus_mahasiswa(daftar_mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa.nim == nim:
            daftar_mahasiswa.remove(mahasiswa)
            print("Mahasiswa berhasil dihapus!")
            return
    print("Mahasiswa tidak ditemukan!")

def main():
    daftar_mahasiswa = []
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Edit Mahasiswa")
        print("3. Lihat Data Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_mahasiswa(daftar_mahasiswa)
        elif pilihan == "2":
            edit_mahasiswa(daftar_mahasiswa)
        elif pilihan == "3":
            lihat_data(daftar_mahasiswa)
        elif pilihan == "4":
            hapus_mahasiswa(daftar_mahasiswa)
        elif pilihan == "5":
            print("Terimakasih sudah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
