#!/usr/bin/python3
"""This helps in defining the integer add function."""

def add_integer(a, b=98):
    """Addition of a and b as integer.
    Any float value is converted to integer before addition.
    Raises:
        TypeError: if value a or b is non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
