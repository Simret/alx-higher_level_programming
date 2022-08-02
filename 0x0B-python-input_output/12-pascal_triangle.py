#!/usr/bin/python3
"""A module that contains a function returning a list of integers for the Pascal's triangle"""


def pascal_triangle(n):
    """Arguments: n, Return"""
    lis = []
    if n <= 0:
        return lis

    for i in range(n):
        lis.append([])
        lis[i].append(1)
        for m in range(1, i):
            lis[i].append(lis[i - 1][m - 1] + lis[i - 1][m])
        if n != 0 and i != 0:
            lis[i].append(1)
    return lis
