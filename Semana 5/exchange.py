list = [8, 5, 3, 2, 1, 6, 1]


def exchange(lst):
    first_element = lst.pop(0)
    last_element = lst.pop(-1)

    lst.append(first_element)
    lst.insert(0, last_element)

    return lst


print(exchange(list))
