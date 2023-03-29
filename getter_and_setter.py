# @property + @setter => getter and setter in the pythonic mode

class Pen:
    def __init__(self, color):
        self.color = color
        self._pen_cap_color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def cap_color(self):
        return self.pen_cap_color

    @cap_color.setter
    def cap_color(self, value):
        self.pen_cap_color = value


pen = Pen('Black')
pen.color = 'Blue'
print(pen.color)

pen.cap_color = 'Red'
print(pen.cap_color)
