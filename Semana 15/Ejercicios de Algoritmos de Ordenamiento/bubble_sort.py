def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break

    return lst


numbs = [3, 2, 9, 1, 5, 6]

sorted_numbers = bubble_sort(numbs)

print(sorted_numbers)