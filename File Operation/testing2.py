# filename = 'testing_word'
# count = 0
# new_lines = []
#
# with open(filename, 'r') as file:
#     for line in file:
#         words = line.split()
#         new_words = []
#         for word in words:
#             word = word.lower()
#             if "gunung" in word:
#                 count += 1
#                 word = word.replace("gunung", "pegunungan")
#             new_words.append(word)
#         new_line = " ".join(new_words)
#         new_lines.append(new_line)
#
# with open(filename, 'w') as file:
#     file.writelines(new_lines)
#
# print(f'Banyak kata gunung: {count}')


import csv

with open('Dataset-1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)
