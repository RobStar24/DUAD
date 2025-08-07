my_list = [10, 20, 30, 40, 50, 2]


def get_min(list):
    minimum = list[0]
    for num in list:
        if num < minimum:
            minimum = num

    return f"The minimum value is {minimum}"


print(get_min(my_list))
