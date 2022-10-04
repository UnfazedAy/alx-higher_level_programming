#!/usr/bin/python3
"""Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """
    Returns the multiplication of 2 matrices
    m_a and m_b must be a list integers or floats
    """
    
     #check if the two matrices aren't empty and is a list
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

# check if the contents of m_a and m_b are also a list
# And also contains only integers or floats
    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of list')
    for numbers in row:
        if type(numbers) not in [int, float]:
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of list")
    for numbers in row:
        if type(numbers) not in [int, float]:
            raise TypeError("m_b should contain only integers or floats")
    
    # checks if the m_a, m_b and it's contents aren't empty
    if m_a == [] or m_a ==[[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    # checks if all rows are equal and of the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b should be of the same size")

    # checks if the condition for multiplication are met
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    matrix = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            product = 0
            for k in range(len(m_a[0])):
                product += m_a[i][k] * m_b[k][j]
            new_row.append(product)  
        matrix.append(new_row)
    return matrix
