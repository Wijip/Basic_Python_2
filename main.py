teks = "Koding Akademi Surabaya"
teks_list = ["Koding", "Akademi", "Surabaya"]

f = open("file.txt", "w")
f.write(teks)
f.writelines(teks_list)
f.close()