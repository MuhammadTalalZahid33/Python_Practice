import math

class Shape:
    def area(self):
        return 0  # default implementation


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height




shapes = [
    Circle(5),
    Rectangle(10, 4),
    Triangle(6, 8)
]

for shape in shapes:
    print(f"The area is: {shape.area():.2f}")
