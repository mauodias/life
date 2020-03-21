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

    @property
    def speed(self):
        return self._speed

    def walk(self, angle=0):
        self.x += math.cos(math.radians(angle))*self.speed
        self.y += math.sin(math.radians(angle))*self.speed

    def tick(self):
        pygame.draw.circle(self._screen, self.color, self.position, self.size)
        self.walk()
