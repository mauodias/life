from color import Color
import math
import pygame

class Cell:

    def __init__(self, screen, x=0, y=0, size=10, color=Color.BLUE, speed=1):
        self._x = x
        self._y = y
        self._size = size
        self._color = color
        self._speed = speed
        self._screen = screen

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        newpos = value
        width = self._screen.get_width() - self.size
        if value > width:
            newpos = width
        elif value < self.size:
            newpos = self.size
        self._x = newpos

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        newpos = value
        height = self._screen.get_height() - self.size
        if value > height:
            newpos = height
        elif value < self.size:
            newpos = self.size
        self._y = newpos

    @property
    def position(self):
        return (self.x, self.y)

    @property
    def size(self):
        return self._size

    @property
    def color(self):
        return self._color.value

    @property
    def speed(self):
        return self._speed

    def walk(self, angle=90):
        self.x += math.cos(math.radians(angle))*self.speed
        self.y += math.sin(math.radians(angle))*self.speed

    def tick(self):
        pygame.draw.circle(self._screen, self.color, self.position, self.size)
        self.walk()
