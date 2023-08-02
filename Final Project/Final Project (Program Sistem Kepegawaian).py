class Pegawai:
    def __init__(self, nama, status_kerja, tahun_masuk, gaji):
        self.nama = nama
        self.status_kerja = status_kerja
        self.tahun_masuk = tahun_masuk
        self.gaji = gaji

class SistemInformasiPegawai:
    def __init__(self):
        self.pegawai_list = []

    def tambah_pegawai(self): # untuk menambah data pegawai
        nama = input("Masukkan nama pegawai: ")
        status_kerja = input("Masukkan status kerja (full time, part time, internship): ")
        tahun_masuk = input("Masukkan tahun masuk pegawai: ")
        gaji = input("Masukkan gaji pegawai: ")
        pegawai_baru = Pegawai(nama, status_kerja, tahun_masuk, gaji)
        self.pegawai_list.append(pegawai_baru)

    def edit_pegawai(self):
        nama = input("Masukkan nama pegawai yang ingin diubah datanya: ")
        for pegawai in self.pegawai_list:
            if pegawai.nama == nama:
                pegawai.status_kerja = input("Masukkan status kerja (full time, part time, internship): ")
                pegawai.tahun_masuk = input("Masukkan tahun masuk pegawai: ")
                pegawai.gaji = input("Masukkan gaji pegawai: ")
                print("Data pegawai telah diubah")
                return
        print("Pegawai tidak ditemukan")

    def tampilkan_pegawai(self):
        if not self.pegawai_list:
            print("Belum ada data pegawai")
            return
        for pegawai in self.pegawai_list:
            print(f"Nama: {pegawai.nama}, Status Kerja: {pegawai.status_kerja}, Tahun Masuk: {pegawai.tahun_masuk}, Gaji: {pegawai.gaji}")

    def hapus_pegawai(self):
        nama = input("Masukkan nama pegawai yang ingin dihapus: ")
        for pegawai in self.pegawai_list:
            if pegawai.nama == nama:
                self.pegawai_list.remove(pegawai)
                print("Data pegawai telah dihapus")
                return
        print("Pegawai tidak ditemukan")

sistem_informasi = SistemInformasiPegawai()

while True:
    print("\n======Sistem Informasi Pegawai======")
    print("1. Tambah Pegawai")
    print("2. Edit Pegawai")
    print("3. Tampilkan Pegawai")
    print("4. Hapus Pegawai")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        sistem_informasi.tambah_pegawai()
    elif pilihan == '2':
        sistem_informasi.edit_pegawai()
    elif pilihan == '3':
        sistem_informasi.tampilkan_pegawai()
    elif pilihan == '4':
        sistem_informasi.hapus_pegawai()
    elif pilihan == '5':
        break
    else:
        print("Pilihan tidak tersedia")



