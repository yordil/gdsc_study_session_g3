class Shape:
    def __init__(self, color) -> None:
        self.color = color

    def get_color(self):
        # print(self.color)
        return self.color


#  if we didn't return the value by default it gonna return None to the child class's super constructor


class Circle(Shape):
    def __init__(self, color, radius) -> None:
        super().__init__(color)
        self.rad = radius

    def area(self):
        return 3.14 * self.rad**2


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.l = length
        self.w = width

    def calculate_area(self):
        return self.l * self.w

    def calculate_preimeter(self):
        return 2 * (self.l + self.w)


rectangle_a = Rectangle("red", 10, 14)
circle_b = Circle("yellow ", 10)


print(rectangle_a.get_color())
print(circle_b.get_color())

print(rectangle_a.calculate_area())
print(circle_b.area())
