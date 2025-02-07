#!/usr/bin/python3
"""Define class"""


class BaseGeometry:
    """ contains one public instance method """
    def area(self):
        """raise an Exception with the message area()
        is not implemented"""
        raise Exception("area() is not implemented")
