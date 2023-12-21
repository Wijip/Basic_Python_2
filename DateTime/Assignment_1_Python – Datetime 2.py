from datetime import datetime,timezone
import pytz as Zone
import time

print("Nomor 1")
now = datetime.now() # mengambil waktu saat ini

# menampilkan waktu dalam format HH:MM:SS
waktu_sekarang = now.strftime("%H:%M:%S")
print(f'Waktu Sekarang {waktu_sekarang}')

zona1 = Zone.timezone('Asia/Jakarta')
zona2 = Zone.timezone('America/New_York')
zona3 = Zone.timezone("Europe/London")
zona4 = Zone.timezone('Australia/Sydney')

waktu = input()
time.sleep(waktu) #-> detik
# total_detik = (menit * 60) + detik)

waktu_zona1 = now.astimezone(zona1).strftime("%H:%M:%S")
waktu_zona2 = now.astimezone(zona2).strftime("%H:%M:%S")
waktu_zona3 = now.astimezone(zona3).strftime("%H:%M:%S")
waktu_zona4 = now.astimezone(zona4).strftime("%H:%M:%S")

print(f'Waktu di Zona 1 (Asia/Jakarta) : {waktu_zona1}')
print(f'Waktu di Zona 2 (America/New_York) : {waktu_zona2}')
print(f'Waktu di Zona 3 (Europe/London) : {waktu_zona3}')
print(f'Waktu di ZOna 4 (Australia/Sydney) : {waktu_zona4}')

print("\nNomor 2")
print(f'Waktu Saat ini di America di Zona (America/New_York) : {waktu_zona2}')

print("\nNomor 3")
print(f'Jika di zona (America/New_York) sekarang jam {waktu_zona2}\nmaka indonesia di zona (Asia/Jakarta) saat ini jam {waktu_zona1}'
      f'\nkarena di amerika memiliki zona waktu yang salah satunya Eastern Standard Time (EST) yang mencakup'
      f'\nkota-kota seperti New York dan Washington D.C'
      f'\nsedangkan Indonesia memiliki zona waktu salah satunya Waktu Indonesia Barat (WIB) yang mencakup'
      f'\nkota kota seperti Jakarta, Bandung. perbedaan antara EST dan WIB adalah 12 jam')

print("\nNomor 4")
menit = int(input("Masukkan Menit : "))
detik = int(input("Masukkan Detik : "))

total_detik = (menit * 60) + detik
print("Waktu berjalan")
for i in range(total_detik):
    menit_sisa, detik_sisa = divmod(total_detik-i,60)
    print("\r{:02d}:{:02d}".format(menit_sisa,detik_sisa), end="")
    time.sleep(1)

print(f'\nWaktu Sudah Selesai : {menit}:{detik}')