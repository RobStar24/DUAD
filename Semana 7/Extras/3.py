def sum_values(list):
    sum_result = 0
    for value in list:
        try:
            float_num = float(value)
            sum_result += float_num
            print(f"{float_num} added correctly")
        except ValueError:
            print(f"Invalid Element: {value}")

    print(f"Total sum: {sum_result}")


my_list = ["10", "manzana", "5.5", "3", "n/a"]
sum_values(my_list)
