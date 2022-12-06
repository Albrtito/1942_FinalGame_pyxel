import math


class Sprite:
    def __init__(self):
        self.__velocidad2 = 2


class Circle():
    def __init__(self, velocidad):
        super().__init__(velocidad)
        self._radius = 3
        self._area = None

    @property
    def radius(self):
        return self._radius

    """
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius must be positive')

        if value != self._radius:
            self._radius = value
            self._area = None
    """

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self.radius ** 2

        return self._area


class CircleTwo(Circle, Sprite):
    def __init__(self):
        super(Circle, self).__init__(4)
        super(Sprite, self).__init__()


circle = Circle()
circle.radius = 3
print(circle.area)
