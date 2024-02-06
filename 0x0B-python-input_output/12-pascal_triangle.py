#!/usr/bin/python3
"""Function of Pascal's Triangle defination"""


def pascal_triangle(n):
    """implementation of Pascal's Triangle.

    Returns a list of lists of integers of the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
