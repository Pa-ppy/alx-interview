#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers for the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # First element of each row is always 1

        # Compute the middle values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Last element is also 1
        triangle.append(row)

    return triangle
