#!/usr/bin/python3
"""Function that checks for inherited class."""

def inherits_from(obj, a_class):
    """This helps to checks if an inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
