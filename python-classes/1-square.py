#!/bin/usr/python3
"""This module contains a class Square that defines a square:
-Private instance attribute: size
-Instantiation with size(no type/value verification)
"""


class Square:
    """This class defines a square"""

    def __init__(self, size):
        """This method initializes a new instance of Square"""
        self.__size = size
