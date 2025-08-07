def highest_number():
    user_list = []

    for i in range(10):
        number = int(input("Enter a number \n"))
        user_list.append(number)

    max_num = user_list[0]

    for num in user_list:
        if num > max_num:
            max_num = num

    print(f"The highest number is: {max_num}")


highest_number()
