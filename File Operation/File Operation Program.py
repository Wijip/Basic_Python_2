import datetime


def parse_log_line(line):
    """
    Mengubah baris log dengan format:
    "YYYY-MM-DD HH:MM:SS - [LEVEL] - Pesan"
    menjadi tuple (timestamp, level, message).
    """
    parts = line.strip().split(" - ")
    timestamp_str = parts[0]
    # Mengonversi string waktu menjadi objek datetime
    timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    # Menghapus tanda kurung siku dari level, misalnya: "[INFO]" -> "INFO"
    level = parts[1].strip()[1:-1]
    message = parts[2]
    return (timestamp, level, message)


def read_log_file(filename):
    """
    Membaca file log dan mengembalikan daftar entry yang sudah diparse.
    """
    entries = []
    with open(filename, "r") as file:
        for line in file:
            if line.strip() != "":
                entry = parse_log_line(line)
                entries.append(entry)
    return entries


def merge_and_sort_logs(file_list):
    """
    Menggabungkan entry dari beberapa file log dan mengurutkannya berdasarkan timestamp.
    """
    merged = []
    for filename in file_list:
        entries = read_log_file(filename)
        merged.extend(entries)
    merged.sort(key=lambda x: x[0])
    return merged


def analyze_logs(entries):
    """
    Menghitung jumlah kemunculan tiap level log.
    """
    level_counts = {}
    for entry in entries:
        level = entry[1]
        if level in level_counts:
            level_counts[level] += 1
        else:
            level_counts[level] = 1
    return level_counts


def write_merged_log(filename, entries):
    """
    Menuliskan entry log yang telah diurutkan ke file dengan format yang sama.
    """
    with open(filename, "w") as file:
        for entry in entries:
            timestamp, level, message = entry
            line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - [{level}] - {message}\n"
            file.write(line)


def main():
    # Daftar file log yang akan digabungkan
    log_files = ["log1.txt", "log2.txt"]

    # Membaca, menggabungkan, dan mengurutkan log
    merged_logs = merge_and_sort_logs(log_files)

    # Menganalisis jumlah entry per level log
    level_counts = analyze_logs(merged_logs)

    print("Statistik Log:")
    for level, count in level_counts.items():
        print(f"{level} : {count}")

    # Menuliskan log gabungan yang telah diurutkan ke file baru
    output_file = "merged_log.txt"
    write_merged_log(output_file, merged_logs)
    print(f"\nMerged log telah disimpan ke file '{output_file}'")


if __name__ == "__main__":
    main()
