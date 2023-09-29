#!/usr/bin/python3
for ascii_letters in range(97, 123):
    if ascii_letters != 101 and ascii_letters != 113:
        print('{}'.format(chr(ascii_letters)), end="")
