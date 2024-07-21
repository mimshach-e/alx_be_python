# Task 2 - Exploring Polymorphism and Method Overriding
import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2 # the **2 or pow(base-number, 2) in-built function is for squaring the base number
