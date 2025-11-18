import pytest

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


def test_small_list():
    assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]


def test_large_list():
    large_list = [i for i in range(100, 0, -1)]
    assert bubble_sort(large_list) == list(range(1, 101))


def test_empty_list_return_empty_list():
    assert bubble_sort([]) == []


def test_invalid_input():
    with pytest.raises(TypeError):
        bubble_sort(123)
    with pytest.raises(TypeError):
        bubble_sort("string")
    with pytest.raises(TypeError):
        bubble_sort(None) 