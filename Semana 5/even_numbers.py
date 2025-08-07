numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even_numbers(list):
    result = []
    for num in list:
        if num % 2 == 0:
            result.append(num)

    return result


print(even_numbers(numbers_list))


# def odd_numbers(list):
#     result = []
#     for num in list:
#         if not num % 2 == 0:
#             result.append(num)

#     return result


# print(odd_numbers(numbers_list))
