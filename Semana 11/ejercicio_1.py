import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)


my_circle = Circle(2)

print(f"The circle area is {my_circle.get_area()}")
