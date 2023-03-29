# @property is a property of the object,
# she is a method that behaves like an attribute 🤯🤯🤯
# is generally used in these cases:
# - as getter
# - to enable setters
# - to execute actions when getting an attibute
# - to avoid breaking client code
# Client code: the code that uses your code

# getter
"""
# Your code
class Pen:
    def __init__(self, color):
        self.ink_color = color

    #getter
    def get_color(self):
        return self.ink_color

########################################

# client code
blue_pen = Pen('Blue')
print(blue_pen.get_color())
print(blue_pen.get_color())
print(blue_pen.get_color())
print(blue_pen.get_color())
print(blue_pen.get_color())
"""

#@property

class Pen:
    def __init__(self, color):
        self.ink_color = color

    @property
    def color(self):
        print('PROPERTY')
        return self.ink_color


##############################
blue_pen = Pen('Blue')
print(blue_pen.color)
print(blue_pen.color)
print(blue_pen.color)
print(blue_pen.color)
print(blue_pen.color)
