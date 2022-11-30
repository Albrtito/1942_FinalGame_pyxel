import math


class Circle:
    def __init__(self):
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

circle = Circle()
circle.radius = 3
print(circle.area)