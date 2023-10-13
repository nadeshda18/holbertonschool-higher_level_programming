#!/usr/bin/python3
"""Function to print string "My name is <first name> <last name>"
Prototype: def say_my_name(first_name, last_name="")
first_name and last_name must be strings otherwise,
-TypeError
        ("first_name must be a string") or
        ("last_name must be a string")
"""


def say_my_name(first_name, last_name=""):
    """
    -TypeError
            ("first_name must be a string") or
            ("last_name must be a string")
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
