# Program Daylight Saving Time (DST)
"""
Daylight Saving Time (DST), atau di Indonesia sering disebut sebagai Waktu Musim Panas (WMP), adalah praktik memajukan waktu
jam selama bulan-bulan yang bercuaca lebih hangat, biasanya satu jam lebih cepat dari waktu standar.
Tujuannya adalah untuk "menyimpan cahaya siang hari" sehingga malam hari datang pada pukul yang lebih lambat.
cara kerjanya?
- Musim semi/awal musim panas: Jam dimajukan satu jam. Misalnya, jika pukul 02.00 dini hari,
akan langsung menjadi pukul 03.00 dini hari. Ini dikenal dengan istilah "spring forward".

- Musim gugur: Jam dimundurkan satu jam kembali ke waktu standar. Misalnya, jika pukul 02.00 dini hari,
akan kembali menjadi pukul 01.00 dini hari. Ini dikenal dengan istilah "fall back".
"""


import datetime
import pytz

def DST():
    print("== Challenge 3: Pemeriskaan Daylight Saving Time (DST) ==")
    date_str = input("Masukkan tanggal (YYYY-MM-DD): ")
    tz_str = input("Masukkan zona waktu (Contoh: Asia/Tokyo): ")
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").replace(hour=12, minute=0, second=0)
    timezone = pytz.timezone(tz_str)
    aware_dt = timezone.localize(dt)

    if aware_dt.dst() != datetime.timedelta(0):
        standar_offset = aware_dt.utcoffset() - aware_dt.dst()
        print("Pada tanggal tersebut DST berlaku")
        print(f"UTC Offset standar: {standar_offset}, dan UTC offset saat ini: {aware_dt.utcoffset()}")
    else:
        print("DST tidak berlaku pada tanggal tersebut")

if __name__ == '__main__':
    DST()