#!/usr/bin/python
"""
Class Bass:
Private class attribute: __nb_objects = 0
Class constructor: def __init__(self, id=None)
    - if id is not None assign the public instance attribute id
    -otherwise increment __nb_objects and assign new value to id

"""


class Base:
    """defines a class Base
    Attributes:
        __nb_objects = number of objects
        id (int) = id of object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init Method
        Args:
            -id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
