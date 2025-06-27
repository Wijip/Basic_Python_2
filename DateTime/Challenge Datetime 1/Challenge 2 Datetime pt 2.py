#generate tanggal dari tanggal yang dinputkan sampai dengan hari terakhir yang di input dengan interval yang dapat ditentukan

import datetime
from datetime import timedelta

def generate_date_range(start_date, end_date, interval):
    if start_date > end_date:
        print("Tanggal mulai harus sama atau sebelum tanggal akhir.")
        return []
    if interval <= 0:
        print("Interval harus lebih besar dari 0.")
        return []

    dates = []
    current = start_date
    while current <= end_date:
        dates.append(current)
        current += timedelta(days=interval)
    return dates

start_input = input("Masukkan tanggal mulai (YYYY-MM-DD): ")
end_input = input("Masukkan tanggal akhir (YYYY-MM-DD): ")
intervals = int(input("Masukkan interval (dalam hari): "))

start_dates = datetime.datetime.strptime(start_input, "%Y-%m-%d").date()
end_dates = datetime.datetime.strptime(end_input, "%Y-%m-%d").date()
date_list = generate_date_range(start_dates, end_dates, intervals)
hari = 0
for date in date_list:
    hari += 1
    print(f"Tanggal ke {hari} = {date}")
