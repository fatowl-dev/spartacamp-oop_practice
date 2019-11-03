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

rectangle1 = Rectangle(height=5, width=6)
assert rectangle1.area() == 30.00
assert rectangle1.diagonal() == 7.81

rectangle2 = Rectangle(height=3, width=3)
assert rectangle2.area() == 9.00
assert rectangle2.diagonal() == 4.24

# rectangle1 = Rectangle(height=5, width=6)
# rectangle1.area()  # 30.00
# rectangle1.diagonal()  # 7.81
#
# rectangle2 = Rectangle(height=3, width=3)
# rectangle2.area()  # 9.00
# rectangle2.diagonal()  # 4.24