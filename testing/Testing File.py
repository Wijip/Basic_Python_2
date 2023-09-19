class Employee:
    def __init__(self, nomer_induk, nama, status_kerja, tahun_masuk, gaji):
        self.nomer_induk = nomer_induk
        self.nama = nama
        self.status_kerja = status_kerja
        self.tahun_masuk = tahun_masuk
        self.gaji = gaji

    def display_info(self):
        print("Nomer Induk:", self.nomer_induk, "Nama:", self.nama, "Status Kerja:", self.status_kerja, "Tahun Masuk:",
              self.tahun_masuk, "Gaji:", self.gaji, )
        print("=============================================================================")


class EmployeeDatabase:
    def __init__(self):
        self.pegawai_list = []

    def tambah_pegawai(self, pegawai):
        self.pegawai_list.append(pegawai)
        print("Pegawai berhasil ditambahkan.")

    def edit_pegawai(self, nomer_induk, new_status_kerja, new_tahun_masuk, new_gaji):
        for pegawai in self.pegawai_list:
            if pegawai.nomer_induk == nomer_induk:
                pegawai.status_kerja = new_status_kerja
                pegawai.tahun_masuk = new_tahun_masuk
                pegawai.gaji = new_gaji
                print("Data pegawai berhasil diubah.")
                return
        print("Pegawai tidak ditemukan.")

    def tampilkan_pegawai(self):
        if not self.pegawai_list:
            print("Data pegawai kosong.")
        else:
            for pegawai in self.pegawai_list:
                pegawai.display_info()

    def hapus_pegawai(self, nomer_induk, nama):
        for pegawai in self.pegawai_list:
            if pegawai.nomer_induk == nomer_induk and pegawai.nama == nama:
                self.pegawai_list.remove(pegawai)
                print("Data pegawai berhasil dihapus.")
                return
        print("Pegawai tidak ditemukan.")


def main():
    database = EmployeeDatabase()

    while True:
        try:
            print("\n=== Menu Utama ===")
            print("1. Tambah Pegawai")
            print("2. Edit Pegawai")
            print("3. Tampilkan Pegawai")
            print("4. Hapus Pegawai")
            print("5. Keluar")
            choice = int(input("Masukkan pilihan (1/2/3/4/5): "))

            if choice == 1:
                nomer_induk = input("Masukkan nomer induk pegawai: ")
                nama = input("Masukkan nama pegawai: ")
                status_kerja = input("Masukkan status kerja (full time/part time/internship): ")
                tahun_masuk = int(input("Masukkan tahun masuk: "))
                gaji = (input("Masukkan gaji: "))
                pegawai = Employee(nomer_induk, nama, status_kerja, tahun_masuk, gaji)
                database.tambah_pegawai(pegawai)

            elif choice == 2:
                nomer_induk = input("Masukkan nomer induk pegawai yang akan diubah datanya: ")
                new_status_kerja = input("Masukkan status kerja baru: ")
                new_tahun_masuk = int(input("Masukkan tahun masuk baru: "))
                new_gaji = float(input("Masukkan gaji baru: "))
                database.edit_pegawai(nomer_induk, new_status_kerja, new_tahun_masuk, new_gaji)

            elif choice == 3:
                database.tampilkan_pegawai()

            elif choice == 4:
                nomer_induk = input("Masukkan nomer induk pegawai yang akan dihapus: ")
                nama = input("Masukkan nama pegawai yang akan dihapus: ")
                database.hapus_pegawai(nomer_induk, nama)

            elif choice == 5:
                print("Terima kasih telah menggunakan Sistem Informasi Pegawai.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
        except ValueError:
            print("\nInput Kosong atau tidak berupa Angka")
        # except Exception as e:
        #     print("Terjadi Kesalahan")


if __name__ == "__main__":
    main()
