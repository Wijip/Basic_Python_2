class SPG:
    def __init__(self, nama, status, tahun, gaji):
        self.nama = nama
        self.status = status
        self.tahun = tahun
        self.gaji = gaji

    def cetak(self):
        print("Nama Pegawai : ", self.nama)
        print("Status       : ", self.status)
        print("Tahun        : ", self.tahun)
        print("Gaji         : ", self.gaji)

    def setEdit(self, nama=None, status=None, tahun=None, gaji=None):
        if nama is not None:
            self.nama = nama
        if status is not None:
            self.status = status
        if tahun is not None:
            self.tahun = tahun
        if gaji is not None:
            self.gaji = gaji


daftar_pegawai = []
loop = True

print("Selamat Datang Di Sistem Informasi Pegawai")
print("Menu : ")
print("1. Tambah Data       ")
print("2. Hapus Data        ")
print("3. Tampilkan Data    ")
print("4. Edit Data Pegawai ")
print("0. Keluar            ")

while loop:
    menu = input("\nMasukan Menu : ")

    if menu == "1":
        pegawai = SPG(input("Masukkan nama : "), input("Masukkan Status : "), input("Masukkan Tahun : "), input("Masukkan Gaji : "))
        daftar_pegawai.append(pegawai)

    elif menu == "2":
        nama = input("Masukkan nama pegawai yang ingin dihapus: ")
        for pegawai in daftar_pegawai:
            if pegawai.nama == nama:
                daftar_pegawai.remove(pegawai)
                print(f"Data pegawai {nama} berhasil dihapus.")
                break
        else:
            print(f"Pegawai dengan nama {nama} tidak ditemukan.")

    elif menu == "3":
        if daftar_pegawai:
            for idx, pegawai in enumerate(daftar_pegawai, start=1):
                print(f"\nPegawai ke-{idx}:")
                pegawai.cetak()
        else:
            print("Tidak ada data pegawai.")

    elif menu == "4":
        nama = input("Masukkan nama pegawai yang ingin diedit: ")
        for pegawai in daftar_pegawai:
            if pegawai.nama == nama:
                new_nama = input("Masukkan nama baru (kosongkan jika tidak ingin mengganti): ")
                new_status = input("Masukkan status baru (kosongkan jika tidak ingin mengganti): ")
                new_tahun = input("Masukkan tahun baru (kosongkan jika tidak ingin mengganti): ")
                new_gaji = input("Masukkan gaji baru (kosongkan jika tidak ingin mengganti): ")
                pegawai.setEdit(
                    nama=new_nama if new_nama else None,
                    status=new_status if new_status else None,
                    tahun=new_tahun if new_tahun else None,
                    gaji=new_gaji if new_gaji else None
                )
                print(f"Data pegawai {nama} berhasil diedit.")
                break
        else:
            print(f"Pegawai dengan nama {nama} tidak ditemukan.")

    elif menu == "0":
        loop = False
    else:
        print("Command not found.")
