import csv
import os


def main():
    input_filename = "datasetFinal.csv"
    output_dir = "filter"

    # Buat folder output jika belum ada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Nama file output
    output_file_female = os.path.join(output_dir, "Pengguna_Javascript_Perempuan.csv")
    output_file_male = os.path.join(output_dir, "Pengguna_Javascript_Laki_Laki.csv")

    with open(input_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Header baris pertama

        # Cari indeks kolom-kolom penting:
        try:
            # Kolom Kelamin (misalnya: "Kelamin") biasanya berada di index 3
            gender_index = header.index("Kelamin")
        except ValueError:
            print("Kolom 'Kelamin' tidak ditemukan dalam header CSV.")
            return

        try:
            # Kolom komunitas JavaScript berada di index 5 (sesuai dengan susunan header)
            community_index = header.index(
                "Adakah komunitas JavaScript di sekitar tempat tinggal kamu? Jika ada, boleh disebutkan nama komunitasnya apa saja. Boleh meetup, telegram grup, WhatsApp, FB group dan sebagainya")
        except ValueError:
            print("Kolom komunitas JavaScript tidak ditemukan dalam header CSV.")
            return

        # Buka file output untuk ditulisi
        with open(output_file_female, 'w', newline='', encoding='utf-8') as female_file, \
                open(output_file_male, 'w', newline='', encoding='utf-8') as male_file:

            female_writer = csv.writer(female_file)
            male_writer = csv.writer(male_file)

            # Tulis header pada masing-masing file output
            female_writer.writerow(header)
            male_writer.writerow(header)

            # Iterasi tiap baris dan proses filtering
            for row in reader:
                # Pastikan baris memiliki cukup kolom untuk menghindari error
                if len(row) <= max(gender_index, community_index):
                    continue

                gender = row[gender_index].strip().lower()
                community = row[community_index].strip().lower()

                # Cek apakah baris ini termasuk yang mengikuti JavaScript.
                # Kita gunakan kriteria: jika pada kolom komunitas terdapat substring "js" atau "javascript"
                if ("js" in community) or ("javascript" in community):
                    if gender == "perempuan":
                        female_writer.writerow(row)
                    elif gender == "laki-laki":
                        male_writer.writerow(row)

    print("Filtering selesai.")
    print(f"File untuk pengguna JavaScript Perempuan disimpan di '{output_file_female}'")
    print(f"File untuk pengguna JavaScript Laki-laki disimpan di '{output_file_male}'")


if __name__ == "__main__":
    main()
