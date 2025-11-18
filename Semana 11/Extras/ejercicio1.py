class Rectangle:
    def __init__(self):
        self.width = self.get_positive_num("Enter the rectangle's width:\n")
        self.height = self.get_positive_num("Enter the rectangle's height:\n")

    def get_positive_num(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    print("Please enter a positive number")
                else:
                    return value

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


my_rectangle = Rectangle()

area = my_rectangle.get_area()
perimeter = my_rectangle.get_perimeter()

print(f"The area of your rectangle is {area}, and the perimeter is {perimeter}")
