def sum_your_number():
    users_num = int(input("Enter a number \n"))
    i = 1
    sum = 0
    while i <= users_num:
        sum += i
        i += 1

    print(f"The result of the sum is {sum}")


sum_your_number()
