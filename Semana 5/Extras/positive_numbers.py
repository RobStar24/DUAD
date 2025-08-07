my_list = [3, 6, 0, -2, 4]


def positive_numbers(list):
    counter = 0

    for num in list:
        if num <= 0:
            counter += 1

    if counter > 0:
        print("There is at least one negative number or zero.")
    else:
        print("All numbers are positive")


positive_numbers(my_list)
