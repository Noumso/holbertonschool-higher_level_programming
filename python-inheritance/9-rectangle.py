#!/usr/bin/python3
""" Define class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """init"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area"""
        return self.__height * self.__width

    def __str__(self):
        """str"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
