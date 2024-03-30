def fahrenheit():
    fahren = (9/5 * celc) + 32
    print("Suhu dalam Fahrenheit:", fahren)

def kelvin():
    kel = celc + 273
    print("Suhu dalam Kelvin:", kel)


# celc = int(input("Masukkan suhu Celcius: "))
# fahrenheit()
# kelvin()
def main():
    global celc
    celc = int(input("Masukkan Celcius "))
    fahrenheit()
    kelvin()

if __name__ == "__main__":
    main()
