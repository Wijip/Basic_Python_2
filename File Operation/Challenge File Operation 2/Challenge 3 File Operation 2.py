import csv


def main():
    input_file = "../datasetFinal.csv"
    output_file = "Pivot_Framework_By_Gender.csv"

    # Dictionary untuk menyimpan pivot
    # pivot[framework] = {"Laki-laki": count, "Perempuan": count, "Total": count}
    pivot = {}

    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        framework_field = "Kamu sedang tertarik belajar tentang framework apa?"
        gender_field = "Kelamin"

        for row in reader:
            framework_data = row.get(framework_field, "").strip()
            gender = row.get(gender_field, "").strip()
            if framework_data == "":
                continue
            # Jika terdapat banyak framework yang dipisahkan dengan koma, pecah datanya
            frameworks = [fw.strip() for fw in framework_data.split(",") if fw.strip()]

            for fw in frameworks:
                if fw not in pivot:
                    pivot[fw] = {"Laki-laki": 0, "Perempuan": 0, "Total": 0}
                if gender.lower() in ["laki-laki", "laki laki", "laki"]:
                    pivot[fw]["Laki-laki"] += 1
                elif gender.lower() in ["perempuan", "wanita"]:
                    pivot[fw]["Perempuan"] += 1
                pivot[fw]["Total"] += 1

    with open(output_file, "w", newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Framework", "Laki-laki", "Perempuan", "Total"])
        for fw, counts in pivot.items():
            writer.writerow([fw, counts["Laki-laki"], counts["Perempuan"], counts["Total"]])

    print(f"Pivot table selesai. Hasil disimpan di '{output_file}'.")


if __name__ == "__main__":
    main()
