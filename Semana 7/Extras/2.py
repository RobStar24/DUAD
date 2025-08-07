def parse_to_int(list):
    print("Result:")
    for value in list:
        try:
            integer = int(value)
            print(f"'{value}' converted to {integer}")
        except ValueError:
            print(f"Unable to convert element: '{value}'")


my_list = ["4", "hola", "10", "5.2"]
parse_to_int(my_list)
