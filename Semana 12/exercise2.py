from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius**2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


circle = Circle(5)
print(f"Circle Perimeter: {circle.calculate_perimeter()}")
print(f"Circle Area: {circle.calculate_area()}")

square = Square(4)
print(f"Square Perimeter: {square.calculate_perimeter()}")
print(f"Square Area: {square.calculate_area()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle Perimeter: {rectangle.calculate_perimeter()}")
print(f"Rectangle Area: {rectangle.calculate_area()}")
