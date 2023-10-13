#!/usr/bin/python3
"""Write a function that prints a square with the character #.
Prototype: def print_square(size):
Size is the size length of the square
Size must be an integer
    -TypeError ("size must be an integer")
Size is less than 0 raise
    -ValueError ("size must be >= 0")
Size is a float and is less than 0
    -TypeError ("size must be an integer")
"""


def print_square(size):
    """Prints a square with the character #"""
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print("#" * size)
