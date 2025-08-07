import random

def guess_the_number():
    secret_number = random.randint(1, 10)

    while True:
        guessed_number = input("Guess a number between 1 and 10 \n")

        if not guessed_number.isdigit():
            print("Please enter a valid number.")
            continue

        guessed_number = int(guessed_number)

        if guessed_number < 1 or guessed_number > 10:
            print("Remember to chose a number between 1 and 10")
        elif guessed_number == secret_number:
            print("Congratulations, you got it right!!!")
            break
        else:
            print("You missed, try again")

guess_the_number()