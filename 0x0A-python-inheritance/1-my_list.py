#!/usr/bin/python3
"""contains a module with a class MyList that inherits from list"""

class MyList(list):
    """defines a class Mylist that inherit from a list"""
    def __init__(self):
      """initializes the object"""
      super().__init__()

    def print_sorted(self):
        """
        A function that prints out a list in ascending order
        """
        sortedlist = sorted(self)
        print(sortedlist)
