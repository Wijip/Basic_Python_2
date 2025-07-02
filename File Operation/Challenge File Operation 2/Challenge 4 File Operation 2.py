import csv


def main():
    input_file = "../datasetFinal.csv"
    output_file = "datasetFinal_clean.csv"

    cleaned_rows = []
    seen_rows = set()  # Untuk mendeteksi duplikat

    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        cleaned_rows.append(header)  # simpan header

        # Ambil indeks kolom Kelamin (asumsikan kolom ada)
        gender_index = header.index("Kelamin")

        for row in reader:
            # Representasi tuple digunakan untuk mendeteksi duplikat
            row_tuple = tuple(row)
            if row_tuple in seen_rows:
                continue
            seen_rows.add(row_tuple)

            # Normalisasi kolom Kelamin tanpa blok try/except
            if len(row) > gender_index:
                gender = row[gender_index].strip().lower()
                if gender in ["laki-laki", "laki laki", "laki"]:
                    row[gender_index] = "Laki-laki"
                elif gender in ["perempuan", "wanita"]:
                    row[gender_index] = "Perempuan"
                else:
                    row[gender_index] = gender.capitalize()
            cleaned_rows.append(row)

    with open(output_file, "w", newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)

    print(f"Data cleaning selesai. File bersih disimpan di '{output_file}'.")


if __name__ == "__main__":
    main()
