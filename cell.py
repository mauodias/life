from color import Color

class Cell:

    def __init__(self, x=0, y=0, size=10, color=Color.BLUE):
        self._x = x
        self._y = y
        self._size = size
        self._color = color

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def position(self):
        return (self.x, self.y)

    @property
    def size(self):
        return self._size

    @property
    def color(self):
        return self._color.value

    def walk(self):
        self.y += 1
