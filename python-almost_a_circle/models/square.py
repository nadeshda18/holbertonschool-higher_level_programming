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
Setter should assign width and height with the same value
Setter should have the same value validation as Rectangle for width and height
Update the class Square by adding the public method
def update(self, *args, **kwargs) that assigns attributes:
    *args is the list of arguments - no-keyword arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
    **kwargs can be thought of as a double pointer to a dictionary:
        key/value (keyword arguments)
    **kwargs must be skipped if *args exists and is not empty
Each key in this dictionary represents an attribute to the instance


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

    def update(self, *args, **kwargs):
        """update method"""
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
