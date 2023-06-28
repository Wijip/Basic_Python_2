import csv
import time

with open('Dataset-1.csv') as csv_file: # membuka file .csv
    csv_reader = csv.reader(csv_file, delimiter=",")  #membaca data didalam file yang tedapat 2 parameter yaitu csv_file dan delimiter, dimana fungsi delimiter untuk memberikan permisah, pada contoh kali ini menggunakan tanda ","
    print(csv_reader)
    for row in csv_reader: # perulangan yang digunakan untuk membaca tiap baris data pada file
        print(row)
        time.sleep(1)



"""
persing file, atau mengubah data yang berbentuk csv ke dalam bentuk lain seperti list atau dictionary
pertama yang harus dilakukan adalah membuat list atau dictionary kosong untuk menyimpan data pada file csv.
"""
# persing file csv ke list
# data = []
# with open('Dataset-1.csv') as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter=",")
#     for row in csv_reader:
#         data.append(row)
#
# for row in data:
#     print(row)


# print("\n")
# # persing file csv ke dictionary
# data = []
# with open('Dataset-1.csv') as csv_file_1:
#     csv_reader = csv.DictReader(csv_file_1)
#     for row in csv_reader:
#         data.append(row)
# for baris in data:
#     print(baris)



#Menulis File CSV
"""
Menulis Dala list ke CSV dapat menggunakan fungsi writerow()
"""
# with open('Dataset-1.csv', mode='a') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(["13", "Ahmad", "Coding Explorer 1.0", "Surabaya"])


#Menulis Data dicitonary ke CSV
"""
Menulis data dicitonary pada dasarnya sama menulis data list ke csv
hanya saja jenis penulisan diganti menjadi Dictwrite().
"""

# with open('Dataset-1.csv', mode='a') as csv_file_2:
#     fieldnames = ['No','Nama','Course','Kota']
#     writer = csv.DictWriter(csv_file_2, fieldnames=fieldnames)
#     writer.writerow({'No':'14','Nama':'Nama','Course':'Python Basic Programming','Kota':'Denpasar'})
