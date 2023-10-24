#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle:
Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)::
    -Call the super class with id, x, y, width and height -
    -this super call will use the logic of the __init__ of the Rectangle class.
    The width and height must be assigned to the value of size
You must not create new attributes for this class, use all attributes of Rect
As reminder: a Square is a Rectangle with the same width and height
All width, height, x and y validation must inherit from Rectangle -
same behavior in case of wrong data
The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> -
in our case, width or height
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init Method
        Args:
            -size (int)
            -x (int)
            -y (int)
            -id (int)
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    @property
    def size(self):
        """getter for width"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
