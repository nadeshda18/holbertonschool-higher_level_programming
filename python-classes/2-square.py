#!/usr/bin/python3
"""This module contains a class Square that defines a square
-Private instance attribute is size
-Instantiation with size(no type/value verification)
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
