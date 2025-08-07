def sum_of_list(list):
    result = 0
    for num in list:
        result += num

    return result


numbers = [4, 6, 2, 29]


result = sum_of_list(numbers)
print(result)
