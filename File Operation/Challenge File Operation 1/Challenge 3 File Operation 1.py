import datetime

def diary_filter():
    input_file = "diary.txt"
    output_file = "filtered_diary.txt"

    keyword = input("Masukkan keyword: ").lower()
    start_date_str = input("Masukkan tanggal mulai (YYYY-MM-DD): ")
    end_date_str = input("Masukkan tanggal akhir (YYYY-MM-DD): ")

    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()

    filtered_lines = []

    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if line == "":
                continue

            timestamp_str = line[:19]
            entry_date = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S").date()
            if start_date <= entry_date <= end_date and keyword in line.lower():
                filtered_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as outfile:
        for line in filtered_lines:
            outfile.write(line + "\n")

    print("Filtering selesai, hasil disimpan di '{}'.".format(output_file))

if __name__ == "__main__":
    diary_filter()
