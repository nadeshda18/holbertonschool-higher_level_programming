#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)
and returns the number of characters written:
Prototype: def write_file(filename="", text=""):
You must use the with statement
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
"""


def write_file(filename="", text=""):
    """Writes a UTF-8 encoded text file."""

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
