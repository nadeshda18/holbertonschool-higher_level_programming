#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines after
each of these characters: ., ? and :
Prototype: def text_indentation(text):
Text must be a string
    -TypeError ("text must be a string")
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """Prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            print(i, end="")
            if i == '.' or i == '?' or i == ':':
                print("\n")
                flag = 0
