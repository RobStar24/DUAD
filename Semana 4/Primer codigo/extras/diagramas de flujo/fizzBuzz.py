def fizz_buzz():
    num = int(input("Enter a number \n"))

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print("Your number is not a FizzBuzz")


fizz_buzz()
