def sort_words(str):
    words_list = str.split("-")
    words_list.sort()
    sorted_words = "-".join(words_list)

    return sorted_words


words = "python-variable-funcion-computadora-monitor"


result = sort_words(words)
print(result)
