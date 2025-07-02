data = [
    [1,2],
    [9,5]
]

data1 = 1,5,3,"data"
data2 = ("askla", "data 2")
data3 = data1 + data2
print(data3)

#tidak bisa rubah, di hapus, di tambah

minuman = (
    ("Kopi","Susu","Teh"),
    ("Jus Apel","Jus Melon","Jus Jeruk"),
    ("Es Kopi","Es Campur","Es Teler")
)
print(minuman[1][1])

item_web = "KodingAkademi", 123, "https://www.kodingakademi.id/"

username, password, link = item_web
print(username)
print(password)
print(link)

for i in item_web:
    print(i)