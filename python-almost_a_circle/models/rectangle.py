#!/usr/bin/python3
""" class Rectangle that inherits "Base"
Private instance Attributes, with it own
public getter and setter
    -__width -> width
    -__height -> height
    -__x -> x
    -__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Class methods:
    super class with id
    assign each argument to the right attribute
"""


from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Method
        Args:
            -width (int)
            -height (int)
            -x (int)
            -y (int)
            -id (int)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        self.__y = value

    @property
    def id(self):
        """getter for id"""
        return self.__id

    @id.setter
    def id(self, value):
        """setter for id"""
        self.__id = value
