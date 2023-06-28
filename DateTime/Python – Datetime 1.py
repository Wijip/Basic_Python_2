from datetime import datetime, timezone # cara mengimport 1 class dari dalam modul

date = datetime.now()

print(f'Format 1 : {date.strftime("%d/%m/%y")}')
print(f'Format 2 : {date.strftime("%c")}')
print(f'Format 3 : {date.strftime("%A, %d, %B, %Y")}')

date2 = date.strftime("%A, %d %B %Y")
date3 = date.strptime(date2, "%A, %d %B %Y")

print(date2)
print(date3)