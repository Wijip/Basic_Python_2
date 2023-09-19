import os, msvcrt

data_directory = 'datanew'
list_file = 'datanew/datanew/all.txt'

def load_destinations_from_file(file_path):
    destinations = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                destinations.append(line.strip())
    return destinations

def load_all():
    all = []
    if os.path.exists(list_file):
        with open(list_file, 'r') as file:
            for line in file:
                all.append(line.strip())
    return all

def list_destination():
    all = load_all()
    if all:
        for a in all:
            print(a)

def kategori():
    destination_type = input("\nPilih Kategori wisata yang ingin kamu kunjungi"
                             " : \n - pantai\n - alam (selain pantai)\n - seni"
                             "\n - budaya\n -  pilihanmu (Masukkan teks) : ")
    file_path = os.path.join(data_directory, f"{destination_type.lower()}.txt")
    destinations = load_destinations_from_file(file_path)
    if destinations:
        print("\nPilih salah satu destinasi berikut : ")
        for index, destination in enumerate(destinations, start=1):
            print(f"{index}.{destination}")
        user_choice = input("Pilihanmu (masukkan teks) : ")
        file_path2 = os.path.join(data_directory,f"{user_choice.lower()}.txt")
        lanjutan = load_destinations_from_file(file_path2)
        if lanjutan:
            print("\nBerikut adalah tempat wisata sesuai yang kamu pilih : ")
            for index, destination in enumerate(lanjutan, start=1):
                print(f"{index}. {destination}")
        return ""

def main():
    while True:
        pilihan = input("Selamat Datang! ayo tentukan destinasi wisaata di pulau"
                        "bali sesuai dengan keinginanmu.\n1. Daftar Seluruh Wisata"
                        "\n2. Pilih Wisata berdasarkan katerogri\n0. Keluar\n"
                        "Pilihanmu (Masukkan Angka) : ")
        if pilihan == "1":
            list_destination()
        elif pilihan == "2":
            kategori()
        elif pilihan == "0":
            break
        print("\nPress any key to continue...")
        msvcrt.getch()  # Menunggu pengguna menekan tombol
        os.system('cls')  # Menghapus layar

if __name__ == "__main__":
    if not os.path.exists(data_directory):
        print("Direktori tidak tersedia")
    else:
        main()