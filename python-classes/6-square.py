#!/usr/bin/python3
"""This module contains a class Square that defines a square
Private instance attribute: size:
Property def size(self): to retrieve it
Property setter def size(self, value): to set it:
Private instance attribute: position:
Property def position(self): to retrieve it
Property setter def position(self, value): to set it
Instantiation with optional size and optional position
def __init__(self, size=0, position=(0, 0))
Public instance method: def area(self)
Public instance method: def my_print(self):
that prints in stdout the square with the character #:
"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """This method initializes a new instance of Square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """This method returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """This method sets the position of the square
        Raises:
            TypeError if not an integer
            ValueError if size if <0
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This method returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
