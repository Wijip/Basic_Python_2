def text_statistics():
    input_file = "document.txt"
    output_file = "document_stats.txt"

    total_lines = 0
    total_words = 0
    total_chars = 0  # tanpa spasi
    word_freq = {}

    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if line == "":
                continue
            total_lines += 1
            words = line.split()
            total_words += len(words)
            total_chars += sum(len(word) for word in words)
            for word in words:
                word_lower = word.lower()
                if word_lower in word_freq:
                    word_freq[word_lower] += 1
                else:
                    word_freq[word_lower] = 1

    # Temukan kata dengan frekuensi tertinggi
    most_freq_word = None
    max_count = 0
    for word, count in word_freq.items():
        if count > max_count:
            max_count = count
            most_freq_word = word

    avg_words_per_line = total_words / total_lines if total_lines > 0 else 0

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write("Text File Statistics\n")
        outfile.write("Total lines: {}\n".format(total_lines))
        outfile.write("Total words: {}\n".format(total_words))
        outfile.write("Total characters (tanpa spasi): {}\n".format(total_chars))
        outfile.write("Most frequent word: '{}' dengan {} kemunculan\n".format(most_freq_word, max_count))
        outfile.write("Rata-rata kata per baris: {:.2f}\n".format(avg_words_per_line))

    print("Statistik selesai. Hasil disimpan di '{}'.".format(output_file))

if __name__ == "__main__":
    text_statistics()
