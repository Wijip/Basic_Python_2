#menghitung jumlah hari kerja antar senin sampai dengan jumat tanpa memperhatikan tanggal merah antara hari senin sampai dengan jumat

import datetime
from datetime import timedelta

def count_working_days(start_date: datetime.date, end_date: datetime.date):
    working_days = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            working_days += 1
        current_date += timedelta(days=1)
    return working_days

start_input = input("Masukkan tanggal mulai (YYYY-MM-DD): ")
end_input   = input("Masukkan tanggal akhir (YYYY-MM-DD): ")

start_dates = datetime.datetime.strptime(start_input, "%Y-%m-%d").date()
end_dates   = datetime.datetime.strptime(end_input, "%Y-%m-%d").date()

print("Jumlah hari kerja:", count_working_days(start_dates, end_dates))
