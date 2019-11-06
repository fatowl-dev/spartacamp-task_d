# 仕様を満たすためにちょっとひねくれた実装してみる
# サンプルにprintがあると課程
import math


class CalcResult:
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f'{self.value:.2f}'

    def __float__(self):
        return self.value

    def __int__(self):
        return int(self.value)


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return CalcResult(self.width * self.height)

    def diagonal(self):
        return CalcResult(math.sqrt(self.width ** 2 + self.height ** 2))


if __name__ == '__main__':
    rectangle1 = Rectangle(height=5, width=6)
    print(rectangle1.area())  # 30.00
    print(rectangle1.diagonal())  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    print(rectangle2.area())  # 9.00
    print(rectangle2.diagonal())  # 4.24

    print(int(rectangle1.area()) * int(rectangle2.diagonal()))  # 120
