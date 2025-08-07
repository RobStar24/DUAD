def secret_number():
    while True:
        secret = 7

        guess = int(input("Guess the number between 1 and 10 \n"))

        if guess <= 10 and guess > 0:
            if guess == secret:
                print("Congratulations!! You guessed right!!!")
                break
            else:
                print("You failed, try again")
                continue
        else:
            print("Pick a different number, remember it has to be between 1 and 10")
            continue


secret_number()
