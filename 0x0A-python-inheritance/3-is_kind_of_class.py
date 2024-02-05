#!/usr/bin/python3
"""A function that checks for inherited class."""


def is_kind_of_class(obj, a_class):
    """Instance or inherited instance of a class.

    Args:
        obj (any): Instance to check.
        a_class (type): Class to match the type of instance to
    Returns:
        Instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
