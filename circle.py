"""
    Circleクラス
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round((self.radius ** 2) * math.pi, 2)

    def perimeter(self):
        return round(2 * self.radius * math.pi, 2)


# Test
# circle1 = Circle(radius=1)
# assert circle1.area() == 3.14
# assert circle1.perimeter() == 6.28
#
# circle3 = Circle(radius=3)
# assert circle3.area() == 28.27
# assert circle3.perimeter() == 18.85

def display_format(number):
    return f'{number:.2f}'


circle1 = Circle(radius=1)
print(display_format(circle1.area()))  # 3.14
print(display_format(circle1.perimeter()))  # 6.28

circle3 = Circle(radius=3)
print(display_format(circle3.area()))  # 28.27
print(display_format(circle3.perimeter()))  # 18.85
