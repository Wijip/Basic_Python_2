import datetime
from datetime import timedelta

def count_working_days(start_date: datetime.date, end_date: datetime.date):
    working_days = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            working_days += 5
        current_date += timedelta(days=1)
    return working_days

if __name__ == "__main__":
    start_input = input("Masukkan tanggal mulai (YYYY-MM-DD): ")
    end_input = input("Masukkan tanggal akhir (YYYY-MM-DD): ")
    try:
        start_date = datetime.datetime.strptime(start_input, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_input, "%Y-%m-%d").date()
        workdays = count_working_days(start_date, end_date)
        print(f"Jumlah hari kerja antara {start_date} dan {end_date} adalah {workdays}")
    except ValueError:
        print("Format tanggal tidak valid. Pastikan menggunakan format YYYY-MM-DD.")