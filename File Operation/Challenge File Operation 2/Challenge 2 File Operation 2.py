import csv, os

def main():
    survey_file = "survey.csv"
    cities_file = "cities.csv"
    output_file = "Joined_Survey_Cities.csv"

    # Baca cities.csv
    cities_dict = {}
    with open(cities_file, newline='', encoding="utf-8") as cf:
        reader = csv.DictReader(cf)
        for city in reader:
            key = city["Domisili"].strip().lower()
            cities_dict[key] = city

    joined_rows = []
    with open(survey_file, newline='', encoding="utf-8") as sf:
        reader = csv.DictReader(sf)

        # Debug: tunjukkan header
        print("Survey fields:", reader.fieldnames)

        # Temukan nama kolom Domisili yang benar
        join_key = next(h for h in reader.fieldnames
                        if "domisili saat ini" in h.lower())
        print("Using join_key =", join_key)

        # siapkan field output
        survey_fieldnames = reader.fieldnames
        cities_fieldnames = [k for k in next(iter(cities_dict.values())).keys()
                             if k.lower() != "domisili"]
        output_fieldnames = survey_fieldnames + cities_fieldnames

        # join
        for row in reader:
            city_raw = row[join_key].strip().lower()
            if city_raw in cities_dict:
                new = row.copy()
                for k in cities_fieldnames:
                    new[k] = cities_dict[city_raw].get(k, "")
                joined_rows.append(new)

    # tulis hasil
    with open(output_file, "w", newline='', encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=output_fieldnames)
        writer.writeheader()
        writer.writerows(joined_rows)

    print("Join selesai, hasil di", output_file)

if __name__ == "__main__":
    main()
