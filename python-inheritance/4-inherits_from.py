#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """Return True or False"""
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
