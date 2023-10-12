#!/usr/bin/python3
"""This module contains a class Square that defines a square:
-Private instance attribute: size
-Instantiation with size(size: def __init__(self, size=0)
"""


class Square:
    """This class defines a square

    Attributes:
        __size (int): size of the square
    """

    def __init__(self, size=0):
        """This method initializes a new instance of Square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
