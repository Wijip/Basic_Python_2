def generate_contacts(n):
    with open("contacts.txt", "w", encoding="utf-8") as f:
        for i in range(1, n+1):
            name = f"Contact{i:03d}"
            pattern = i % 5
            if pattern == 1:
                part1 = f"{i:03d}"
                part2 = f"{(i*7)%10000:04d}"
                number = f"0812-{part1}-{part2}"
            elif pattern == 2:
                part1 = f"{i:04d}"
                part2 = f"{(i*13)%10000:04d}"
                number = f"+62 812 {part1}-{part2}"
            elif pattern == 3:
                z = f"{i*5:07d}"
                number = f"(0812){z}"
            elif pattern == 4:
                q = f"{i*7:07d}"
                number = f"0812{q}"
            else:
                r = f"{i:03d}"
                s = f"{(i*3)%1000:03d}"
                number = f"+62-812-0{r}-{s}"
            f.write(f"{name}, {number}\n")

if __name__ == '__main__':
    data = int(input("Masukkan jumlah data: "))
    generate_contacts(data)
    print(f"Contact.txt dengan {data} data berhasil dibuat")