#menentukan nomor minggu dalam satu tahun

import datetime

date_input = input("Masukkan tanggal (YYYY-MM-DD): ")

date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
week_number = date_obj.isocalendar()[1]

print(f"Nomor minggu dari tanggal {date_obj} adalah: {week_number}")
