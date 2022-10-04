#!/usr/bin/python3
"""say my name: playing around with strings"""


def say_my_name(first_name, last_name):
    """
    Args: first_name, last_name
    result = My name is first_name, last_name
    e.g My name is Ayomide Soniyi
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
