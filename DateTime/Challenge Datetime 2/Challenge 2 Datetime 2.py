#program menghitung selisih waktu antar zona waktu

import datetime
import pytz

def zona_waktu():
    print("== Challenge 2: Menghitung selisih waktu antara zona waktu yang berbeda ==")
    tz_str1 = input("Masukkan zona waktu pertama (contoh: Asia/Jakarta): ")
    tz_str2 = input("Masukkan zona waktu kedua (contoh: Asia/Singapore): ")
    timezone1 = pytz.timezone(tz_str1)
    timezone2 = pytz.timezone(tz_str2)
    now_utc = datetime.datetime.now(pytz.utc)
    now1 = now_utc.astimezone(timezone1)
    now2 = now_utc.astimezone(timezone2)

    diff_seconds = abs(now1.utcoffset().total_seconds() - now2.utcoffset().total_seconds())
    diff_minutes = int(diff_seconds // 60)
    hours = diff_minutes // 60
    minutes = diff_minutes % 60
    print(f"Selisih waktu antara {tz_str1} dan {tz_str2} adlaah : {hours} jam dan {minutes} Menit")

if __name__ == '__main__':
    zona_waktu()