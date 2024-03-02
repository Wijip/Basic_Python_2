from datetime import datetime
import pytz as Zone

indonesia = datetime.now()

Murika = Zone.timezone('America/New_York')
zona1 = Zone.timezone('Asia/Jakarta')

waktu = indonesia.astimezone(Murika).strftime("%H:%M:%S")
waktu_zona1 = indonesia.astimezone(zona1).strftime("%H:%M:%S")


print(waktu)
print(f'Waktu di Zona 1 (Asia/Jakarta) : {waktu_zona1}')