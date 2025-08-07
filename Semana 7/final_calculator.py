def show_menu():
    print(
        "OPTIONS MENU\n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Clear result\n"
        "6. Exit"
    )
    print("-" * 48)


def get_option():
    while True:
        try:
            option = int(input("Select an option (1 - 6): "))
            if 1 <= option <= 6:
                return option
            else:
                raise ValueError
        except ValueError:
            print("Error: Select a valid option (1-6)")


def get_number():
    while True:
        try:
            number = float(input("Enter the number: "))
            return number

        except ValueError:
            print("Error: Please enter a valid number.")


def add(current_value):
    print("Performing SUM")
    new_number = get_number()
    return current_value + new_number


def subtract(current_value):
    print("Performing SUBTRACTION")
    new_number = get_number()
    return current_value - new_number


def multiply(current_value):
    print("Performing MULTIPLICATION")
    new_number = get_number()
    return current_value * new_number


def divide(current_value):
    print("Performing DIVISION")
    while True:
        try:
            new_number = get_number()
            if new_number != 0:
                return current_value / new_number
            else:
                raise ValueError
        except ValueError:
            print("Error: You cannot divide by zero")


def calculator():
    print("\n")
    print("Welcome to the Calculator!!\n")
    current_value = 0
    while True:
        try:
            show_menu()
            print(f"Current value: {current_value}")

            option = get_option()

            if option == 1:
                current_value = add(current_value)

            elif option == 2:
                current_value = subtract(current_value)

            elif option == 3:
                current_value = multiply(current_value)

            elif option == 4:
                current_value = divide(current_value)

            elif option == 5:
                print("CLEAR RESULT")
                current_value = 0
                print("Result Cleared. Current Value: 0")

            elif option == 6:
                print("Goodbye!")
                break

        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")
            break


if __name__ == "__main__":
    calculator()
