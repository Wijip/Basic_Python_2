#program Penjadwal acara/Reminder Lintas Zona waktu
import datetime

import pytz

class EventReminder:
    def __init__(self, event_time_str, zones):
        self.event_time_utc = datetime.datetime.strptime(event_time_str, "%Y-%m-%d %H:%M:%S")
        self.event_time_utc = pytz.utc.localize(self.event_time_utc)
        self.zones = zones

    def display_reminders(self):
        for zone in self.zones:
            tz = pytz.timezone(zone)
            local_event_time = self.event_time_utc.astimezone(tz)
            now_local = datetime.datetime.now(tz)
            diff = local_event_time - now_local
            diff_minutes = diff.total_seconds() / 60
            print(f"\nZona Waktu: {zone}")
            print(f"Waktu acara lokal {zone}: {local_event_time.strftime('%Y-%m-%d %H:%M:%S')}")
            if 0 <= diff_minutes <= 15:
                print("Reminder: Acara akan dimulai dalam 15 Menit")
            else:
                print(f"Acara dimulai dalam {int(diff_minutes)} Menit")
def main():
    print("== Challenge 4: Penjadwalan Acara / Rimender Lintas Zona waktu ==")
    event_time_str = input("Masukkan waktu acara dalam UTC (YYYY-MM-DD HH:MM:SS): ")
    zones_str = input("Masukkan zona waktu (Pisahkan dengan koma, Contoh: Asia/Jakarta, Europe/London, America/New_York): ")
    zones = [zone.strip() for zone in zones_str.split(",")]
    reminder = EventReminder(event_time_str, zones)
    reminder.display_reminders()

if __name__ == '__main__':
    main()