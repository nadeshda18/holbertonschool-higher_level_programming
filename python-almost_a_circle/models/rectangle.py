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
Raises:
    TypeError: value must be an integer
    ValueError: value must be > 0
Public method def area(self): return area value of Rectangle
Public method def display(self): prints in stdout the Rectangle
Public method def update(self, *args):
    -1st argument: id attribute
    -2nd argument: width attribute
    -3rd argument: height attribute
    -4th argument: x attribute
    -5th argument: y attribute
    -"no-keyword arguments" Argument order is super important
-Update Public method def update(self, *args, **kwargs):
    -**kwargs must be skipped if *args exist or is not empty
    -each key in this dictionary represents an attribute to the instance
    -"key-worded arguments" Argument oder is NOT important
    """


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

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
        """setter for width
        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height
        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x
        Raises:
        TypeError must be an integer
        ValueError must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y
        Raises:
        TypeError must be an integer
        ValueError must be >= 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def id(self):
        """getter for id"""
        return self.__id

    @id.setter
    def id(self, value):
        """setter for id"""
        self.__id = value

    def area(self):
        """return area of Rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """adding the public method
        assign arguments to each attribute
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
