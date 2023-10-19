#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle.
Instantiation with size: def __init__(self, size)::
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return,
the square description: [Square] <width>/<height>
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square, inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size
        Args:
            size (int): size (private)
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of square"""
        return self.__size ** 2

    def __str__(self):
        """Return string representation of square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
