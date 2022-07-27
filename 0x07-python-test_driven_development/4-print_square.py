#!/usr/bin/python3
"""4-print_square module that prints a square with the character #"""


def print_square(size):
    """
    Takes an argument size
    size must be an integer
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
