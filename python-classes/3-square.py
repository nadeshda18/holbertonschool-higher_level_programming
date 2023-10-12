#!/usr/bin/python3
"""This module contains a class Square that defines a square
-Private instance attribute is size
-Instantiation with size(size: def __init__(self, size=0)
-Public instance method: def area(self)
"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """This method initializes a new instance of Square
        Raises:
            TypeError if not an integer
            ValueError if size if <0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """This method returns the area of the square"""
        return self.__size ** 2
