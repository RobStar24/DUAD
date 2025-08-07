list_a = ["city", "country", "population"]
list_b = ["New York", "USA", 8419600]


def dictionary_creator(list1, list2):
    dictionary = {}

    for i in range(len(list1)):
        dictionary[list1[i]] = list2[i]

    return dictionary


print(dictionary_creator(list_a, list_b))
