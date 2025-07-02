import datetime


def Catat():
    filename = "diary.txt"
    print("== Chalenge File Operation 1: Diary/Catatan Harian ==")
    print("Masukkan catatan harian. ketik 'exit' untuk berhenti.")

    with open(filename, 'a') as file:
        while True:
            entry = input("Catatan: ")
            if entry.lower() == "exit":
                break
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {entry}\n")

    print("\nIsi Diary")
    with open(filename, "r") as file:
        contents = file.read()
        print(contents)

if __name__ == '__main__':
    Catat()