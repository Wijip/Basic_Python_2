file_path = 'Assignment_replace_teks'
with open(file_path, 'r') as key:
    lines = key.readlines()

with open('Data_Replace.txt', 'w') as write:
    write.writelines(lines)

filename = 'Data_Replace.txt'
count = 0
new_lines = []

with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        new_words = []
        for word in words:
            word = word.lower()
            if "gunung" in word:
                count += 1
                word = word.replace("gunung", "pegunungan")
            new_words.append(word)
        new_line = " ".join(new_words)
        new_lines.append(new_line)

with open(filename, 'w') as file:
    file.writelines(new_line)

print(f'Banyak kata gunung : {count}')
