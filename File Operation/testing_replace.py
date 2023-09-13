# Membaca teks dari file
with open('testing.txt', 'r') as file:
    teks_deskripsi = file.read()

# Menghitung berapa kali kata "gunung" muncul dalam teks
jumlah_kata_gunung = teks_deskripsi.lower().count("gunung")

# Mengganti kata "gunung" dengan kata "pegunungan"
teks_deskripsi_terganti = teks_deskripsi.replace("gunung", "pegunungan")

# Menampilkan jumlah kata "gunung" yang ditemukan
print(f"Jumlah kata 'gunung' dalam teks: {jumlah_kata_gunung}")

# Menyimpan teks yang sudah diubah kembali ke file
with open('teks_deskripsi_terganti.txt', 'w') as file:
    file.write(teks_deskripsi_terganti)

# Menampilkan teks yang sudah diubah
print(teks_deskripsi_terganti)
