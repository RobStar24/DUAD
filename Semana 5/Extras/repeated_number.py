def repeated_number():
    my_list = []

    print(
        "First you are going to create a list of numbers, then choose one number to know how many times it repeats"
    )

    while True:
        user_input = input("Enter a number, when you are done type 'exit' \n")

        if user_input == "exit":
            break

        if user_input.isdigit():
            my_list.append(int(user_input))
        else:
            print("Please enter a valid number")

    while True:
        number_to_find = input("Enter the number to find: \n")

        if number_to_find.isdigit():
            number_to_find = int(number_to_find)
            break
        else:
            print("Please enter a valid number")

    count = 0

    for num in my_list:
        if num == number_to_find:
            count += 1

    print(f"The number {number_to_find} appears {count} times")


repeated_number()
