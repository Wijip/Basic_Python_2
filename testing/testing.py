def hitung(*nilai):
    jumlah = sum(nilai)
    avg = jumlah / 10
    return jumlah, avg


def main():
    print(hitung(3,4,5,8,3,7,3,10,4,12,45))


if __name__ == '__main__':
    main()