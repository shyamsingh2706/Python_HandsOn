''' Create an abstract class called Shape
    inherit it to create other classes Circle , Rectangle & Triangle to calculate Area & Perimeter
    Use property decorator ( getter method ) to define Area & Perimeter as attribute of the class inheritted from Shape'''


from math import pi, sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return pi * self._radius * self._radius

    @property
    def perimeter(self):
        return 2 * pi * self._radius


class Rectangle(Shape):
    def __init__(self,height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    #return list contain of three sides
    @property
    def getsides(self):
        return [self._side_a, self._side_b, self._side_c]

    # based on Heron Formula
    # http://en.wikipedia.org/wiki/Heron's_formula
    @property
    def area(self):
        s = (self._side_a + self._side_b + self._side_c)/2
        return sqrt(s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c))

    @property
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c


cir = Circle(10)
print (f"Circle radius is {cir.radius}")
print (f"Circle area is {cir.area}")
print (f"Circle perimeter is {cir.perimeter}")

Rec = Rectangle(10,10)
print (f"Rectangle width is {Rec.width}")
print (f"Rectangle height is {Rec.height}")
print (f"Rectangle area is {Rec.area}")
print (f"Rectangle perimeter is {Rec.perimeter}")

Tri = Triangle(10,10,10)
print (f"Triangle Sides are {Tri.getsides}")
print (f"Triangle area is {Tri.area}")
print (f"Triangle perimeter is {Tri.perimeter}")
