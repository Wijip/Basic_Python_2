#chalenge interval time / Generate Daftar Tanggal dalam Rentang tertentu

import datetime
from datetime import timedelta

start_input = input("Masukkan tanggal mulai (YYYY-MM-DD): ")
end_input   = input("Masukkan tanggal akhir (YYYY-MM-DD): ")
interval    = int(input("Masukkan interval (dalam hari): "))

start_date = datetime.datetime.strptime(start_input, "%Y-%m-%d").date()
end_date = datetime.datetime.strptime(end_input, "%Y-%m-%d").date()

current = start_date

while current <= end_date:
    print(current)
    current += timedelta(days=interval)
