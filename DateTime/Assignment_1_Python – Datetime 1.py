from datetime import datetime, timezone

date = datetime.now()
print("Nomor 1")
print(date)

print("\nNomor 2")
print(f'Format date 1 : {date.strftime("%a, %d %B %Y")}')
print(f'Format date 2 : {date.strftime("%H:%M:%S")}')
print(f'Format date 3 : {date.strftime("%A, %b %d, %H:%M:%S %Y")}')
print(f'Format date 4 : {date.strftime("%A, %d %B %Y")}')

print("\nNomor 3")
print(f'Format date 5 : {date.strftime("%d %B , %A, %H:%M:%S %Y")}')