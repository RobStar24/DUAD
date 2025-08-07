text = "Magna fugiat veniam aliquip incididunt id cupidatat ad aliqua reprehenderit."


def get_the_letter(str):
    counter = 0
    letter = input(
        "Enter the letter you want to know how many times it appears in the text. \n"
    ).lower()

    str = str.lower()

    for char in str:
        if letter == char:
            counter += 1

    if counter == 1:
        return f"The letter '{letter}' has been found {counter} time."
    else:
        return f"The letter '{letter}' has been found {counter} times."


result = get_the_letter(text)
print(result)
