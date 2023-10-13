#!/usr/bin/python3
"""A Function to add two integers
Prototype: def add_integer(a, b=98)
a and b must be integers or floats
    -TypeError ("a must be an integer")
    -TypeError ("b must be an integer")
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """function to add two integers
    Raises:
    -cast float into integer
    -raise TypeError if a or b is not an integer
    Return: a + b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
