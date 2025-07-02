# Fungsi untuk membaca file, menghitung kemunculan kata "Gunung" atau "gunung", dan menggantinya dengan "pegunungan"
def process_file_final(filename):
    # Membuka file untuk membaca
    with open(filename, 'r', encoding='utf-8') as file:
        # Membaca isi file
        content = file.read()

        # Menghitung jumlah kata "Gunung" dan "gunung"
        count_gunung = content.count('Gunung') + content.count('gunung')

        # Mengganti "Gunung" dengan "Pegunungan" hanya sekali, dan "gunung" dengan "pegunungan"
        updated_content = content.replace('Gunung', 'Pegunungan')  # Mengganti 'Gunung' dengan 'Pegunungan'
        updated_content = updated_content.replace('gunung', 'pegunungan')  # Mengganti 'gunung' dengan 'pegunungan'

    # Menyimpan perubahan ke file baru (atau bisa overwrite file lama)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    # Mengembalikan hasil jumlah kata yang ditemukan
    return count_gunung

# Nama file yang akan diproses
filename = 'learn4.txt'

# Memproses file dan mendapatkan hasil jumlah kata "Gunung" atau "gunung"
count = process_file_final(filename)

# Menampilkan hasil
print(f'Jumlah kemunculan kata "Gunung" atau "gunung": {count}')
