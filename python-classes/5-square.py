#!/usr/bin/python3
"""Module containing the Square class"""


class Square:
    """The Square class"""
    def __init__(self, size=0):
        """Initializing an instance of Square

        Args:
            size (int): The size of the Square instance. Default value is 0.
        """
        self.size = size

    @property
    def size(self):
        """int: Value of 'size'"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area of the instance

        Returns:
            int: Value of 'size'
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square with hashtags using the 'size'"""
        if self.__size is not 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
