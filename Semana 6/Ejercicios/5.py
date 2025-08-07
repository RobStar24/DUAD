def count_case_types(str):
    lower_case = 0
    upper_case = 0

    for char in str:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1

    return f"There's {upper_case} upper cases and {lower_case} lower cases"


phrase = "I Love Nation Sushi"


result = count_case_types(phrase)
print(result)
