def number_30():
    print(
        "Enter three numbers and we will see if any of them is 30 or if their sum is 30."
    )
    number1 = int(input("Enter the fist number \n"))
    number2 = int(input("Enter the second number \n"))
    number3 = int(input("Enter the third number \n"))

    if number1 == 30 or number2 == 30 or number3 == 30:
        print("Correct")
    elif number1 + number2 + number3 == 30:
        print("Correct")
    else:
        print("Incorrect")


number_30()
