#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Arg text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    special_characters = [".", "?", ":"]
    for words in text:
        print(f"{words}", end="")
        if words in special_characters:
            print("\n\n", end="")
