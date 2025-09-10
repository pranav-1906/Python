class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Square(Shape):
    def __init__(self, color, filled, side):
        super().__init__(color,filled)
        self.side = side

    def describe(self):
        super().describe()
        print(f"It's a square with area of {self.side*self.side}")

class Triangle(Shape):
    def __init__(self, color, filled, length, height):
        super().__init__(color,filled)
        self.length = length
        self.height = height

    def describe(self):
        super().describe()
        print(f"It's a triangle with area of {(self.length * self.height)/2}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It's a circle with area of {3.14 *(self.radius*self.radius)}")


square = Square('Red', True, 6)
triangle = Triangle('Blue', False, 7, 8)
circle = Circle('green',True, 5)

square.describe()
triangle.describe()
circle.describe()
