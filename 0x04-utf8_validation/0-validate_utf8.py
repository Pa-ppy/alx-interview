#!/usr/bin/python3
"""
UTF-8 validation module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes
    :return: True if valid UTF-8, else False
    """
    num_bytes = 0

    for byte in data:
        # Mask to get only the last 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count number of leading 1's
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) == 0b0:
                num_bytes = 0
            else:
                return False
        else:
            # Continuation bytes must start with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
