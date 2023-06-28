# kode untuk replace teks dalam file tanpa menggunakan modul

search_text = "Koding akademi"
replacet_text = "Koding Akademi 2.0"
with open('kodingakademi.txt',mode='r') as file:
    data = file.read()
    data = data.replace(search_text, replacet_text)

with open('kodingakademi.txt', mode='w') as file:
    file.write(data)

# searching and replacing text menggunakan library pathlib2

from pathlib2 import Path
search_text = "Koding Akademi"
replacet_text = "Koding Akademi 2.0"
file = Path('kodingakademi.txt', mode='r')
data = file.read_text()
data = data.replace(search_text, replacet_text)
file.write_text(data)

# searching dan replacing text menggunakan modul regex

import re

search_text = "Koding Akademi"
replacet_text = "Koding Akademi 2.0"

with open('kodingakademi.txt', mode='r+') as f:
    file = f.read()
    file = re.sub(search_text, replacet_text, file)
    f.seek(0)
    f.write(file)
    f.truncate()

# searching and replacing text dengan file input
from fileinput import FileInput
search_text = "Koding Akademi"
replacet_text = "Koding Akademi 2.0"

with FileInput("kodingakademi.txt", inplace=True, backup=".bak") as f:
    for line in f:
        print(line.replace(search_text, replacet_text), end='')