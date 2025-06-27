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

start_date = datetime.datetime.strptime("2022-07-01", "%Y-%m-%d").date()
end_date = datetime.datetime.strptime("2022-07-31", "%Y-%m-%d").date()
print("Jumlah hari kerja:", count_working_days(start_date, end_date))
