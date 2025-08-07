def biggest_number():
    print("Pick three different numbers and I'll give you the biggest among them")

    first_number = int(input("Pick the first number: \n"))
    second_number = int(input("Pick the second number: \n"))
    third_number = int(input("Pick the third number: \n"))

    highest_number = 0

    if first_number > second_number:
        highest_number = first_number
    else:
        highest_number = second_number
    
    if third_number > highest_number:
        highest_number = third_number

    print(f"The biggest number is {highest_number}")

biggest_number()