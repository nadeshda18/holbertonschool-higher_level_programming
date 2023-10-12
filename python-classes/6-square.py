#!/usr/bin/python3
"""This module contains a class Square that defines a square:
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
    """This class defines a square
    Args:
        size (int): size of the square
        position (tuple): position of the square as a tuple
        of 2 positive integers
        Defaults to (0, 0)
    Attributes:
        __size (int): size of the square
        __position (tuple): position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """This method initializes a new instance of Square
        Raises:
            TypeError: if not an integer or position is not
            a tuple of 2 positive integers
            ValueError: if size if less than 0 or position values are
            less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This method returns the size of the square
        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size of the square
        Raises:
            TypeError: if value is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """This method returns the position of the square
        Returns:
            tuple: the position of the square as a
            tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """This method sets the position of the square
        Raises:
            TypeError: if value is not an integer
            ValueError: if position value is less than 0
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise ValueError("position values must be >= 0")

        self.__position = value

    def area(self):
        """This method returns the area of the square
        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character #
        to stdout with a specified position
        if size is equal to 0, print an empty line
        Don't fill lines with spaces when position[1] > 0
        """
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
