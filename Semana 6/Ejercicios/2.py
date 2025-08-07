age = 34


def show_age():
    print(f"My age inside the first function is: {age}")


def have_birthday():
    global age
    age = 35
    print(f"The age after birthday is: {age}")


show_age()
have_birthday()
