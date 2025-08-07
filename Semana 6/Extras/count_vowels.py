vowels = ["a", "e", "i", "o", "u"]
phrase = "Incididunt anim nostrud pariatur est cupidatat anim."


def count_vowels(words):
    counter = 0
    words = words.lower()
    for char in words:
        if char in vowels:
            counter += 1

    return counter


result = count_vowels(phrase)
print(result)
