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
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    count = None
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if count == None:
            count = len(rows)
        elif count != len(rows):
            raise TypeError("Each row of the matrix must have the same size")
        for values in rows:
            if type(values) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by Zero")
    
    new_matrix = [[round(values / div, 2) for values in rows] for rows in matrix]
    return new_matrix
