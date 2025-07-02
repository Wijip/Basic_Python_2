#menhitung umur dari tanggal lahir yang dinputkan

import datetime
from datetime import timedelta

def hitung_usia(birth_input):
    birth_date = datetime.datetime.strptime(birth_input, "%Y-%m-%d").date()
    today = datetime.date.today()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year

        last_day_prev_month = (datetime.date(prev_year, prev_month + 1, 1) - timedelta(days=1)).day
        days += last_day_prev_month
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return years, months, days

birth_input = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
tahun, bulan, hari = hitung_usia(birth_input)
print(f"Usia saat ini: {tahun} tahun, {bulan} bulan, {hari} hari.")
