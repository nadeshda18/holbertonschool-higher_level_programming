#!/usr/bin/python
"""
Class Bass:
Private class attribute: __nb_objects = 0
Class constructor: def __init__(self, id=None)
    - if id is not None assign the public instance attribute id
    -otherwise increment __nb_objects and assign new value to id

"""


import json
import csv


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
    """to_json_string method"""
    if list_dictionaries is None or len(list_dictionaries) == 0:
        return "[]"
    return json.dumps(list_dictionaries)


@classmethod
def save_to_file(cls, list_objs):
    """save_to_file method"""
    objs = []
    if list_objs is not None:
        for obj in list_objs:
            objs.append(obj.to_dictionary())
    filename = cls.__name__ + ".json"
    with open(filename, "w") as f:
        f.write(cls.to_json_string(objs))


@staticmethod
def from_json_string(json_string):
    """from_json_string method"""
    if json_string is None or len(json_string) == 0:
        return []
    return json.loads(json_string)


@classmethod
def create(cls, **dictionary):
    """create method"""
    if cls.__name__ == "Rectangle":
        dummy = cls(1, 1)
    elif cls.__name__ == "Square":
        dummy = cls(1)
    else:
        dummy = None
    if dummy:
        dummy.update(**dictionary)
    return dummy


@classmethod
def load_from_file(cls):
    """load_from_file method"""
    filename = cls.__name__ + ".json"
    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            objs = cls.from_json_string(f.read())
        return [cls.create(**obj) for obj in objs]
    except FileNotFoundError:
        return []
