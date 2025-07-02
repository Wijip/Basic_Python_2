#Menhitung Usia dari tanggal lahir

import datetime
from datetime import timedelta

birth_input = input("Masukkan tanggal lahir (YYYY-MM-DD): ")

birth_date = datetime.datetime.strptime(birth_input, "%Y-%m-%d").date()
today = datetime.date.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    first_day_of_month = datetime.date(today.year, today.month, 1)
    last_day_prev_month = (first_day_of_month - timedelta(days=1)).day
    days += last_day_prev_month

if months < 0:
    years -= 1
    months += 12

print(f"Usia saat ini: {years} tahun, {months} bulan, {days} hari.")