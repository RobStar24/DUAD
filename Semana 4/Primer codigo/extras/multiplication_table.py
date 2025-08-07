def multiplication_table():
    while True:
        number = int(input("Enter a number between 1 and 10: \n"))

        if number > 0 and number <= 10:
            i = 1

            while i <= 12:
                print(f"{number} x {i} = {number * i}")
                i += 1
            break

        else:
            print("Please enter a valid number between 1 and 10")


multiplication_table()
