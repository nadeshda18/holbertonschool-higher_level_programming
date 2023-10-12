#!/usr/bin/python3
"""This module contains a class Square that defines a square
-Private instance attribute is size
-Property def size(self)
-Property setter def size(self, value)
-Instantiation with size(size: def __init__(self, size=0)
-Public instance method: def area(self)
"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """This method initializes a new instance of Square"""
        self.__size = size

    @property
    def size(self):
        """This method returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size of the square
        Raises:
            TypeError if not an integer
            ValueError if size if <0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """This method returns the area of the square"""
        return self.__size ** 2
