nama = input("Masukkan Nama : ")
umur = input("Masukkan Umur : ")
alamt = input("Masukkan alamat : ")

with open('assignment2', 'a') as file:
    file.write(f'{nama} | {umur} | {alamt}\n')

print("Data berhasil disimpan ke dalam file Assignment2")