class Mahasiswa:
    def __init__(self):
        self.data = {}

    def tambah_data(self):
        nama = input("Masukkan nama mahasiswa : ")
        nim = input("Masukkan NIM Mahasiswa : ")
        usia = input("Masukkan usia mahasiswa : ")
        jurusan = input("Masukkan jurusan mahasiswa : ")
        alamat = input("Masukkan alamat mahasiswa : ")

        tahun_masuk = "20" + nim[:2]

        self.data[nim] = {"Nama": nama, "Usia": usia, "Jurusan": jurusan, "Alamat": alamat, "Tahun Masuk": tahun_masuk}

        print("Data mahasiswa berhasil ditambahkan!")

    def tampilkan_data(self):
        print("\n Daftar Mahasiswa")
        print("==================================================================")
        print("NIM\t\tNama\t\tTahun Masuk\t\tJurusan\t\tUsia\t\tAlamat")
        print("==================================================================")

        for nim, info in self.data.items():
            print(f"{nim}\t{info['Nama']}\t\t{info['Tahun Masuk']}\t\t{info['Jurusan']}\t{info['Usia']}\t{info['Alamat']}")
        print("==================================================================")

mahasiswa = Mahasiswa()

while True:
    print("\nSelamat datang di program pendaftaran mahasiswa\nSilahkan pilih menu:")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Keluar")

    pilih = int(input("Masukkan Pilihan Anda (1/2/3) : "))
    if pilih == 1:
        mahasiswa.tambah_data()
    elif pilih == 2:
        mahasiswa.tampilkan_data()
    elif pilih == 3:
        print("Terima kasih telah menggunakan program pendaftaran mahasiswa.")
        break
    else:
        print("Pilihan tidak valid, silahkan masukkan pilihan yang sesuai dengan menu yang tersedia")