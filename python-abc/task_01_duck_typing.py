#!/usr/bin/python3

from abc import ABC, abstractmethod
import math

"""
Importing Module Math
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        """
        Method to be present in each subclass
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Method to be present in each subclass
        """
        pass


class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize Circle with radius
        """
        self.radius = radius

    def area(self):
        """
        Returns the area
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Return the perimeter
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape
    """
    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    the shape_info function using duck typing
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
