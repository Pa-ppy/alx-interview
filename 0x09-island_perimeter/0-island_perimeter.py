#!/usr/bin/python3
"""
This module provides a function to calculate the perimeter
of an island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A 2D grid where 1 represents land
        and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    height = len(grid)

    for i in range(height):
        width = len(grid[i])
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
