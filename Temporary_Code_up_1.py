# generate_contacts.py
def generate_contacts(n=100):
    """
    Menghasilkan file contacts.txt dengan n baris:
    Contact001, <nomor telepon>
    Contact002, <nomor telepon>
    … dst
    Format nomor dibuat bergantian agar ulik pola:
     - 0812-XXX-YYYY
     - +62 812 XXXX YYYY
     - (0812)ZZZZZZZ
     - 0812QQQQQQQ
     - +62-812-0RRR-SSS
    """
    with open("contacts.txt", "w", encoding="utf-8") as f:
        for i in range(1, n+1):
            name = f"Contact{i:03d}"
            pattern = i % 5
            if pattern == 1:
                # 0812-XXX-YYYY
                part1 = f"{i:03d}"
                part2 = f"{(i*7)%10000:04d}"
                number = f"0812-{part1}-{part2}"
            elif pattern == 2:
                # +62 812 XXXX YYYY
                part1 = f"{i:04d}"
                part2 = f"{(i*13)%10000:04d}"
                number = f"+62 812 {part1} {part2}"
            elif pattern == 3:
                # (0812)ZZZZZZZ
                z = f"{i*5:07d}"
                number = f"(0812){z}"
            elif pattern == 4:
                # 0812QQQQQQQ
                q = f"{i*7:07d}"
                number = f"0812{q}"
            else:
                # +62-812-0RRR-SSS
                r = f"{i:03d}"
                s = f"{(i*3)%1000:03d}"
                number = f"+62-812-0{r}-{s}"

            f.write(f"{name}, {number}\n")

if __name__ == "__main__":
    generate_contacts(100)
    print("contacts.txt dengan 100 data berhasil dibuat.")
