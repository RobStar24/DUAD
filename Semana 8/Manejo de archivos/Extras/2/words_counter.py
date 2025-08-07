def count_words(path):
    word_count = 0
    with open(path) as file:
        for line in file:
            words = line.split()
            word_count += len(words)

    return f"This file contains {word_count} words."


path = "Extras/2/text.txt"

result = count_words(path)
print(result)
