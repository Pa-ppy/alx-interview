#!/usr/bin/python3
"""Module for calculating minimum operations to achieve n H characters."""


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters.

    Args:
        n (int): Target number of H characters.

    Returns:
        int: Minimum number of operations, or 0 if impossible.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
