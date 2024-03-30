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
        words = line.splitlines()
        new_words = []
        for word in words:
            # word = word.lower()
            if "gunung" or "Gunung" in word:
                count += 1
                word1 = word.replace("gunung", "pegunungan")
                word2 = word.replace("Gunung", "pegunungan")
            new_words.append(word1)
            new_words.append(word2)
        new_line = " ".join(new_words)
        new_lines.append(new_line)
    with open(filename, 'a') as file:
        file.writelines(new_line)

# with open(filename, 'a') as file:
#     file.writelines(new_line)

print(f'Banyak kata gunung : {count}')
