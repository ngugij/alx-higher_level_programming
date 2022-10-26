#!/usr/bin/python3
"""pascal_triangle module"""


def pascal_triangle(n):
    """returns a list of lists of integers
        representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    tri = [[1]]
    while len(tri) != n:
        tri_rep = tri[-1]
        tmp = [1]
        for i in range(len(tri_rep) - 1):
            tmp.append(tri_rep[i] + tri_rep[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
