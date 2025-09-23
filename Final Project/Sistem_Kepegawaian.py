class Pegawai:
    def __init__(self, nama, status, tahun_masuk, gaji):
        self.nama = nama
        self.status = status
        self.tahun_masuk = tahun_masuk
        self.gaji = gaji

    def edit_data(self, nama=None, status=None, tahun_masuk=None, gaji=None):
        if nama: self.nama = nama
        if status: self.status = status
        if tahun_masuk: self.tahun_masuk = tahun_masuk
        if gaji: self.gaji = gaji

    def tampilkan(self):
        return f"{self.nama:<15} {self.status:<12} {self.tahun_masuk:<12} {self.gaji:<10}"

class SistemInformasiPegawai:
    def __init__(self):
        self.daftar_pegawai = []

    def tambah_pegawai(self):
        nama = input("Masukkan nama: ")
        status = input("Masukkan Status (Full Time/Part Time/Internship): ")
        tahun_masuk = input("Masukkan Tahun Masuk: ")
        gaji = input("Masukkan Gaji: ")
        pegawai_baru = Pegawai(nama, status, tahun_masuk, gaji)
        self.daftar_pegawai.append(pegawai_baru)
        print("Pegawai berhasil ditambahkan\n")

    def tampilkan_pegawai(self):
        if not self.daftar_pegawai:
            print("Tidak ada data pegawai.\n")
            return
        print(f"{'No':<4} {'Nama':<15} {'Status':<12} {'Tahun Masuk':<12} {'Gaji':<10}")
        for i, pegawai in enumerate(self. daftar_pegawai, start=1):
            print(f"{i:<4} {pegawai.tampilkan()}")
        print()

    def edit_pegawai(self):
        self.tampilkan_pegawai()
        index = int(input("Masukkan nomor pegawai yang ingin diedit: ")) -1
        if 0 <= index < len(self.daftar_pegawai):
            nama = input("Nama baru (Kosongkan jika tidak diubah): ")
            status = input("Status baru (Kosongkan jika tidak diubah): ")
            tahun_masuk = input("Tahun masuk baru (Kosongkan jika tidak diubah): ")
            gaji = input("Gaji baru (Kosongkan jika tidak diubah): ")
            self.daftar_pegawai[index].edit_data(
                nama if nama else None,
                status if status else None,
                tahun_masuk if tahun_masuk else None,
                gaji if gaji else None
            )
            print("Data pegawai berhasil dirubah!\n")
        else:
            print("Nomor Pegawai tidak valid\n")

    def hapus_pegawai(self):
        self.tampilkan_pegawai()
        index = int(input("Masukkan nomor pegawai yang ingin dihapus: ")) -1
        if 0 <= index < len(self.daftar_pegawai):
            del self.daftar_pegawai[index]
            print("Pegawai berhasil dihapus!\n")
        else:
            print("Nomor pegawai tidak valid.\n")

    def menu(self):
        while True:
            print("Selamat Datang di Sistem Informasi Pegawai")
            print("Silahkan Memilih Menu:")
            print("1. Tambah Pegawai")
            print("2. Edit Pegawai")
            print("3. Hapus Pegawai")
            print("4. Tampilkan Pegawai")
            print("0. keluar")
            pilihan = input("Pilih Menu: ")
            if pilihan == "1":
                self.tambah_pegawai()
            elif pilihan == "2":
                self.edit_pegawai()
            elif pilihan == "3":
                self.hapus_pegawai()
            elif pilihan == "4":
                self.tampilkan_pegawai()
            elif pilihan == "0":
                print("Terima kasih telah menggunakan sistem ini.")
                break
            else:
                print("Pilihan tidak valid.\n")

sistem = SistemInformasiPegawai()
sistem.menu()