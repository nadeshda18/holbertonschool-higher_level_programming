#!/usr/bin/python3
"""Write a class Student that defines a student by
Public instance attributes:
    first_name
    last_name
    age
Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None):
    that retrieves a dictionary representation of a Student instance
If attrs is a list of strings, only attribute names contained
in this list must be retrieved.
Otherwise, all attributes must be retrieved
"""


class Student:
    """defines a class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        Raises:
        list of strings, only attributes names must be retrieved
        else all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
