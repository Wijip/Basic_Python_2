#menghitung jumlah responden dan umur rata-rata setiap gender
import csv


def main():
    input_file = "../datasetFinal.csv"
    output_file = "Aggregated_Survey_by_Gender.csv"

    groups = {}

    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)

        gender_index = header.index("Kelamin")
        umur_index = header.index("Umur kamu berapa saat ini?")

        for row in reader:
            if len(row) <= max(gender_index, umur_index):
                continue
            gender = row[gender_index].strip()
            umur_str = row[umur_index].strip()
            if umur_str == "":
                continue
            if umur_str.replace('.', '', 1).isdigit():
                umur = float(umur_str)
            else:
                continue
            if gender in groups:
                groups[gender]["count"] += 1
                groups[gender]["sum_age"] += umur
            else:
                groups[gender] = {"count": 1, "sum_age": umur}

    with open(output_file, "w", newline='', encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Kelamin", "Jumlah Responden", "Rata-rata Umur"])
        for gender, data in groups.items():
            count = data["count"]
            avg_age = data["sum_age"] / count if count > 0 else 0
            writer.writerow([gender, count, f"{avg_age:.2f}"])

    print(f"Aggregasi selesai, hasil disimpan di '{output_file}'.")


if __name__ == "__main__":
    main()
