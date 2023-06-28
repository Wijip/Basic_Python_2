import datetime as date
from datetime import datetime
import pytz as zone #modul digunakan untuk mengetahui zona waktu

print(datetime.now()) #untuk mengetahui waktu sekarang
print(date.date(2022, 12, 3)) #merubah integer menjadi objek date atau tanggal
print(date.time(12, 31, 3)) #merubah integer menjadi objek time atau waktu
print(date.datetime(2022, 12, 3, 12, 31, 3)) #merubah integer menjadi format date dan time atau tanggal dan waktu

# print("\nTime Zone")
# for x in zone.all_timezones: #menampilkan seluruh zona waktu
#     print(x)

print("\nwaktu berdasarkan zona waktu")

utc = zone.utc
pst = zone.timezone('America/New_York')
ist = zone.timezone('Asia/Calcutta')

print(f'Current Date Time in UTC : {datetime.now(tz=utc)}')
print(f'Current Date Time in PST : {datetime.now(pst)}')
print(f'Current Date Time in IST : {datetime.now(ist)}')

