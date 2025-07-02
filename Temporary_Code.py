import csv

def is_number(s):
    s = s.strip()
    return s.replace('.', '', 1).isdigit()

def stats(input_file):
    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fields = reader.fieldnames

        # Inisialisasi struktur data
        stats = {}
        for f in fields:
            stats[f] = {'count': 0, 'sum': 0.0, 'min': None, 'max': None}

        # Hitung
        for row in reader:
            for f in fields:
                val = row[f]
                if is_number(val):
                    num = float(val)
                    s = stats[f]
                    s['count'] += 1
                    s['sum'] += num
                    s['min'] = num if s['min'] is None or num < s['min'] else s['min']
                    s['max'] = num if s['max'] is None or num > s['max'] else s['max']

    # Tulis ringkasan statistik
    output_file = input_file.replace('.csv', '_stats.csv')
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Column', 'Count', 'Sum', 'Average', 'Min', 'Max'])
        for f, s in stats.items():
            if s['count'] > 0:
                avg = s['sum'] / s['count']
                writer.writerow([f, s['count'], s['sum'], f"{avg:.2f}", s['min'], s['max']])

    print(f"Statistik selesai. Output: {output_file}")

if __name__ == "__main__":
    fn = input("File CSV untuk di-statistik: ")
    stats(fn)
