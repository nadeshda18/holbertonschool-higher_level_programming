#!/usr/bin/python3
""" Defines a Rectangle class
Private instance attribute: width:
    Property def width(self): to retrieve it
    Property setter def width(self, value): to set it:
Private instance attribute: height:
    Property def height(self): to retrieve it
    Property setter def height(self, value): to set it:
Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
Public instance method: def area(self):
    that returns the rectangle area
Public instance method: def perimeter(self):
    that returns the rectangle perimeter:
print() and str() should print the rectangle with the character #
"""


class Rectangle:
    """This class defines a Rectangle
    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    Raises:
        TypeError: when width/height is no an integer
        ValueError: when width/height less than zero
    print() and str() should print the rectangle with the character #
    """

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle.
        parameters:
            width (int): width of the new rectangle.
            height (int): height of a new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """ This method sets the width of the Rectangle
        Raises:
            TypeError: value is not an integer
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be  >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ This method sets the height of the Rectangle
        Raises:
            TypeError: value is not an integer
            ValueError: value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be  >= 0")
        self.__height = value

    def area(self):
        """ This method returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """ This method returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width * self.__height)

    def __str__(self):
        """ This method returns a string with the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """ This method returns a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
