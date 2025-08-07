def more_than_4():
    print("Please chose 5 words \n")
    word1 = input("Enter the fist word \n")
    word2 = input("Enter the second word \n")
    word3 = input("Enter the third word \n")
    word4 = input("Enter the fourth word \n")
    word5 = input("Enter the fifth word \n")

    words_list = [word1, word2, word3, word4, word5]

    long_words = []

    for word in words_list:
        if len(word) > 4:
            long_words.append(word)

    print(long_words)


more_than_4()
