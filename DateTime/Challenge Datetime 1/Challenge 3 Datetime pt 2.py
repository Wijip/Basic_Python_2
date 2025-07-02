#menentukan nomer Minggu dalam satu tahun

import datetime

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_week_number(date_input):
    if len(date_input) != 10 or date_input[4] != '-' or date_input[7] != '-':
        print("Format tanggal salah. Harap masukkan dengan format YYYY-MM-DD.")
        return None, None

    year_str = date_input[0:4]
    month_str = date_input[5:7]
    day_str = date_input[8:10]

    if not (year_str.isdigit() and month_str.isdigit() and day_str.isdigit()):
        print("Komponen tanggal harus berupa angka.")
        return None, None

    year = int(year_str)
    month = int(month_str)
    day = int(day_str)

    if month < 1 or month > 12:
        print("Bulan tidak valid, Harus antara 1 dan 12")
        return None, None

    days_in_mounth = [31, 29 if is_leap_year(year) else 28,31,30,
                      31,30,31,31,30,31,30,31]
    max_day = days_in_mounth[month - 1]

    if day < 1 or day > max_day:
        print(f"Hari tidak valid. Bulan {month} tahun {year} hanya memiliki {max_day} hari.")
        return None, None

    date_obj = datetime.date(year, month, day)
    week_number = date_obj.isocalendar()[1]
    return date_obj, week_number


date_inputs = input("Masukkan tanggal (YYYY-MM-DD): ")
date_obj, week_number = get_week_number(date_inputs)
if date_obj is not None:
    print(f"Nomor minggu dari tanggal {date_obj} adalah: {week_number}")
