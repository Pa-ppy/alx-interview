#!/usr/bin/python3
"""
Module 0-rotate_2d_matrix
Rotates an n x n 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a square 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): A 2D square matrix.
    """
    n = len(matrix)

    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            # Swap element at (i, j) with (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete rotation
    for row in matrix:
        row.reverse()
