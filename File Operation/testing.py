filename = 'Assignment_replace_teks'
count = 0
with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower()
            if "gunung" in word:
                count += 1

print(f'Banyak kata gunung : {count}')