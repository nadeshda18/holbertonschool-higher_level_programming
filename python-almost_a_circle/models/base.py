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
Static method def from_json_string(json_string): that returns the list of the
JSON string representation json_string:
    -json_string is a string representing a list of dictionaries
    -If json_string is None or empty, return an empty list
    -Otherwise, return the list represented by json_string
Class method def create(cls, **dictionary): that returns an instance with all attributes already set:
    **dictionary can be thought of as a double pointer to a dictionary
    To use the update method to assign all attributes,
    you must create a “dummy” instance before:
Create a Rectangle or Square instance with “dummy” mandatory attributes
    (width, height, size, etc.)
Call update instance method to this “dummy” instance to apply your real values
    You must use the method def update(self, *args, **kwargs)
    **dictionary must be used as **kwargs of the method update
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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            -json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            -**dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
