#!/usr/bin/python3
""" Read a text file (UTS8) and print to stdout
Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
"""


def read_file(filename=""):
    """Reads a UTF-8 encoded text file."""

    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
