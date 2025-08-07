my_list = [10, 20, 30, 40, 50]


def get_above_average(list):
    sum = 0

    for num in list:
        sum += num

    average = sum / len(list)

    above_average = []
    for num in list:
        if num > average:
            above_average.append(num)

    print(f"Average: {average}")
    print(f"New list: {above_average}")


get_above_average(my_list)
