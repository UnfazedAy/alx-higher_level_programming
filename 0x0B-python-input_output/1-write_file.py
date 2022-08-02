#!/usr/bin/python3
"""Writes to a file"""


def write_file(filename="", text=""):
     """
     A function that writes a text file (UTF8)
     and returns the numbers of characters within
     """
     with open(filename, mode='w', encoding='UTF-8') as my_file:
        write = my_file.write(text)
        return write
