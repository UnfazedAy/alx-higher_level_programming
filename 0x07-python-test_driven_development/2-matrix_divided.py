#!/usr/bin/python3
"""2-matrix_divided module"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div
    Takes two args:
    matrix -> A list of list of integers or floats
    div -> A number, integer or float. The divisor
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    count = None
    for numbers in matrix:
        if type(numbers) is not list:
            raise TypeError("matrix must be a matrix"
                            " (list of lists) of integers/floats")
        if count is None:
            count == len(numbers)
        elif count != len(numbers):
            raise TypeError("Each row of the matrix must have the same size")
        for num in numbers:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = [[round(num / div, 2) for num in numbers] for numbers in matrix]
    return new_mat
