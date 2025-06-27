import re

# Fungsi untuk membaca file, menghitung kemunculan kata "Gunung" atau "gunung", dan menggantinya dengan "pegunungan"
def process_file(filename):
    # Membuka file untuk membaca
    with open(filename, 'r', encoding='utf-8') as file:
        # Membaca isi file
        content = file.read()

        # Menghitung jumlah kata "gunung" (dalam berbagai format: 'Gunung', 'gunung')
        count_gunung = len(re.findall(r'\b[Gg]unung\b', content))

        # Mengganti semua kata "Gunung" atau "gunung" dengan "pegunungan"
        updated_content = re.sub(r'\b[Gg]unung\b', 'pegunungan', content)

    # Menyimpan perubahan ke file baru (atau bisa overwrite file lama)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    # Mengembalikan hasil jumlah kata yang ditemukan
    return count_gunung

# Nama file yang akan diproses
filename = 'learn4.txt'

# Memproses file dan mendapatkan hasil jumlah kata "Gunung" atau "gunung"
count = process_file(filename)

# Menampilkan hasil
print(f'Jumlah kemunculan kata "Gunung" atau "gunung": {count}')
