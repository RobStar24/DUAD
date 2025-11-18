
#! FUNCTION 1

def sum_of_list(list):
    result = 0
    for num in list:
        result += num
    return result

def test_sum_of_list():
    assert sum_of_list([4, 6, 2, 29]) == 41

    assert sum_of_list([10]) == 10

    assert sum_of_list([]) == 0


#! FUNCTION 2

def reverse(string):
    result = ""
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    return result

def test_reverse():
    assert reverse("Hello World!") == "!dlroW olleH"

    assert reverse("A") == "A"

    assert reverse("") == ""


#! FUNCTION 3

def count_case_types(str):
    lower_case = 0
    upper_case = 0

    for char in str:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1

    return f"There's {upper_case} upper cases and {lower_case} lower cases"

def test_count_case_types():
    assert count_case_types("I Love Nation Sushi") == "There's 4 upper cases and 12 lower cases"

    assert count_case_types("hello world") == "There's 0 upper cases and 10 lower cases"

    assert count_case_types("HELLO WORLD") == "There's 10 upper cases and 0 lower cases"


#! FUNCTION 4

def sort_words(str):
    words_list = str.split("-")
    words_list.sort()
    sorted_words = "-".join(words_list)
    return sorted_words

def test_sort_words():
    assert sort_words("python-variable-funcion-computadora-monitor") == "computadora-funcion-monitor-python-variable"

    assert sort_words("apple") == "apple"

    assert sort_words("") == ""


#! FUNCTION 5

def is_prime(num):
    if num <= 1:
        return False
    sqrt_floor = int(num**0.5)
    for i in range(2, sqrt_floor + 1):
        if num % i == 0:
            return False
    return True

def get_primes(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

def test_get_primes():
    assert get_primes([1, 4, 6, 7, 13, 9, 67]) == [7, 13, 67]

    assert get_primes([4, 6, 8, 10]) == []

    assert get_primes([2, 3, 5, 7, 11]) == [2, 3, 5, 7, 11]