#!/usr/bin/python3
"""Integers addition"""


def add_integer(a, b=98):
    """
    Adds two numbers
    Takes in two argument a and b
    a - first number input
    b - second number input
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return int(a) + int(b)
