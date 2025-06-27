#Program konversi beberapa zona waktu
import datetime
import pytz


def main():
    print("== Challenge 1: Konversi Waktu Antar Zona Waktu ==")
    dt_str = input("Masukkan tanggal dan waktu (YYYY-MM-DD HH:MM:SS): ")
    tz_str = input("Masukkan zona waktu asal (contoh: Asia/Jakarta): ")

    # Parsing dan localize waktu
    naive_dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    source_tz = pytz.timezone(tz_str)
    aware_dt = source_tz.localize(naive_dt)

    # Daftar zona waktu tujuan
    target_zones = ["Europe/London", "America/Los_Angeles", "Asia/Tokyo", "America/New_York", "America/Santiago", "Asia/Singapore"]
    print("\nWaktu dalam zona waktu berbeda:")
    for zone in target_zones:
        target_tz = pytz.timezone(zone)
        dt_converted = aware_dt.astimezone(target_tz)
        print(f"{zone}: {dt_converted.strftime('%Y-%m-%d %H:%M:%S')} ({zone})")



main()
