import time
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