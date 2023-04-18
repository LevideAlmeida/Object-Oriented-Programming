# python Dunder Methods, Special Methods Magic Methods
# Dunder = Double Underscore = __dunder__
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        return f'({self.x + other.x}, {self.y + other.y})'

    def __gt__(self, other):
        return self.x > other.x

if __name__ == '__main__':
    point1 = Point(1, 15)
    point2 = Point(5, 27)
    point3 = point1 + point2
    print(point3)
    print('Point 1 is greater then point 2:', point1 > point2)
    print('Point 2 is greater then point 1:', point2 > point1)
