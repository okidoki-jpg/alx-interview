#!/usr/bin/python3
"""
Module Doc: pascal_triangle
Calculate pascal triangle given int: n

Attributes:
    n (int): input value

Return:
    2D array
"""


def pascal_triangle(n):
    """
    Pascal Triangle Function
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
