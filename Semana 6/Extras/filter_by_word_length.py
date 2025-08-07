words = ["cielo", "sol", "maravilloso", "día"]


def filter_word_by_length(list):
    word_length = int(input("Enter the minimum number of letters in the word \n"))
    result = []

    for word in list:
        if len(word) > word_length:
            result.append(word)

    return result


result = filter_word_by_length(words)
print(result)
