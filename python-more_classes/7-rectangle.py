#!/usr/bin/python3
""" This module contains a class Rectangle that defines a rectangle:
Private instance attribute: width:
    Property def width(self): to retrieve it
    Property setter def width(self, value): to set it:
Private instance attribute: height:
    Property def height(self)
    Property setter def height(self, value)
Public class attribute number_of_instances:
    Initialized to 0
    Incremented during each new instance instantiation
    Decremented during each instance deletion
Public class attribute print_symbol:
    Initialized to #
    Used as symbol for string representation
    Can be any type
Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
Public instance method: def area(self):
    that returns the rectangle area
Public instance method: def perimeter(self):
    that returns the rectangle perimeter:
print() and str() should print the rectangle with the
    character(s) stored in print_symbol:
repr() should return a string representation of the rectangle
    to be able to recreate a new instance by using eval()
Print the message Bye rectangle... (... being 3 dots not ellipsis)
    when an instance of Rectangle is deleted
"""


class Rectangle:
    """This defines a Rectangle
    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    Raises:
        TypeError: when width/height is no an integer
        ValueError: when width/height less than zero
    print() and str() should print the rectangle with the character #
    repr() should return a string representation of the rectangle
    when an instance of rectangle is deleted, print Bye Rectangle...
    """

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle.
        parameters:
            width (int): width of the new rectangle.
            height (int): height of a new rectangle.
            number of instances incremented
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """ This method sets the width of the Rectangle
        Raises:
            TypeError: when value is not an integer
            ValueError: when value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ This method sets the height of the Rectangle
        Raises:
            TypeError: when value is not an integer
            ValueError: when value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """ This method returns the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """ This method returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """ This method returns the string representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol)*self.__width]*self.__height)

    def __repr__(self):
        """ This method returns the string representation of the Rectangle
        to be able to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ This method prints the message Bye rectangle...
        when an instance of Rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
