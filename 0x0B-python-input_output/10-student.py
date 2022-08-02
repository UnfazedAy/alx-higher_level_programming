#!/usr/bin/pyton3
"""Module for Student"""


class Student:
    """
    A class Student that defines a student by:
    Public instance attributes:
    first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        """
        initializes student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is str:
                    return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
