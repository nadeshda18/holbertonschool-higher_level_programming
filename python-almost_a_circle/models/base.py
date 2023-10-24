#!/usr/bin/python3
"""
Class Bass:
Private class attribute: __nb_objects = 0
Class constructor: def __init__(self, id=None)
    - if id is not None assign the public instance attribute id
    -otherwise increment __nb_objects and assign new value to id
Static method def to_json_string(list_dictionaries):
    -list_dictionaries is a list of dictionaries
    -If list_dictionaries is None or empty, return the string: "[]"
    -Otherwise, return the JSON string representation of list_dictionaries
def save_to_file(cls, list_objs): that writes the JSON string
representation of list_objs to a file:
    -list_objs is a list of instances who inherits of Base -
    example: list of Rectangle or list of Square instances
    -If list_objs is None, save an empty list
    -The filename must be: <Class name>.json - example: Rectangle.json
    -You must use the static method to_json_string (created before)
    -You must overwrite the file if it already exists
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            -list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            -list_objs
        """
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(i.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(new_list))
