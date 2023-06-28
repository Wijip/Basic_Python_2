file_path = 'datasetFinal.csv'

male_data = []
female_data =[]

with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'Laki-laki' in line:
            male_data.append(line)
        elif 'Perempuan' in line:
            female_data.append(line)


with open('filter/Laki-laki.csv', 'w') as male_file:
    male_file.writelines(male_data)

with open('filter/Perempuan.csv', 'w') as female_file:
    female_file.writelines(female_data)

print("Filtering dan penyimpanan berhasil")