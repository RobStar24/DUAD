def get_name():
    while True:
        name = input("Enter your name:\n")
        if name.isdigit():
            raise ValueError("The name cannot be a number")
        return name


def get_age():
    while True:
        try:
            age = int(input("Enter your age:\n"))
            return age
        except ValueError:
            print("Invalid Number")


def main():
    while True:
        try:
            name = get_name()
            age = get_age()
            print(f"Hello {name}, your age is {age}")
            break
        except ValueError as ex:
            print(ex)


if __name__ == "__main__":
    main()
