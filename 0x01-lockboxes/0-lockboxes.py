#!/usr/bin/python3
"""
Module to determine if all boxes can be opened using DFS traversal.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened starting from box 0.

    Args:
        boxes (list of list of int): A list where each index represents a box,
        and the list at each index contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for key in boxes[current]:
                if 0 <= key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n
