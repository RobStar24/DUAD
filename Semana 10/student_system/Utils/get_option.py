def get_option():
    while True:
        try:
            option = int(input("Select an option (1 - 7):"))
            if 1 <= option <= 7:
                return option
            else:
                raise ValueError
        except ValueError:
            print("Error: Select a valid option (1-7)")