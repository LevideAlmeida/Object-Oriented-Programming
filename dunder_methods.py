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

# Python dunder methods __str__ __repr__

class Point:
    def __init__(self, x, y, z='string'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

point1 = Point(4,9)
point2 = Point(2,5)

print(point1)
print(repr(point2))
print(f'{point2!r}')
