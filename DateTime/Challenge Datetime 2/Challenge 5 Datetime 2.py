#Program Penambahan Waktu dan Konversi Zona

import datetime
import pytz
def tambah_zona():
    print("== Challenge 5: Penambahjan waktu dan Konversi Zona ==")
    dt_str = input("Masukkan tanggal dan waktu (YYYY-MM-DD HH:MM:SS): ")
    tz_str = input("Masukkan Zona Waktu asal (Contoh: Asia/Jakarta): ")
    days = int(input("Masukkan jumlah hari yang ingin ditambahkan: "))
    hours = int(input("Masukkan jumlah jam yang ingin ditambahkan: "))
    minutes = int(input("Masukkan jumlah manit yang ingin ditambahkan: "))

    naive_dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    source_tz = pytz.timezone(tz_str)
    aware_dt = source_tz.localize(naive_dt)

    delta = datetime.timedelta(days=days, hours=hours, minutes=minutes)
    new_dt = aware_dt + delta
    target_tz_str = input("Masukkan zona waktu target untuk konversi (Contoh: UTC atau Asia/Tokyo): ")
    target_tz = pytz.timezone(target_tz_str)
    new_dt_converted = new_dt.astimezone(target_tz)
    print("\nWaktu setelah penambahan periode dan konversi: ")
    print(new_dt_converted.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

if __name__ == '__main__':
    tambah_zona()