"""
    Rectangle クラスの実装

    # 仕様
    丸めはroundをつかう
    rectangle1 = Rectangle(height=5, width=6)
    rectangle1.area()  # 30.00
    rectangle1.diagonal()  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    rectangle2.area()  # 9.00
    rectangle2.diagonal()  # 4.24
"""
import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return round(self.height * self.width, 2)

    def diagonal(self):
        return round(math.sqrt(self.height ** 2 + self.width ** 2), 2)


# rectangle1 = Rectangle(height=5, width=6)
# assert rectangle1.area() == 30.00
# assert rectangle1.diagonal() == 7.81
#
# rectangle2 = Rectangle(height=3, width=3)
# assert rectangle2.area() == 9.00
# assert rectangle2.diagonal() == 4.24


rectangle1 = Rectangle(height=5, width=6)
print(f'{rectangle1.area():.2f}')  # 30.00
print(f'{rectangle1.diagonal():.2f}')  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(f'{rectangle2.area():.2f}')  # 9.00
print(f'{rectangle2.diagonal():.2f}')  # 4.24
