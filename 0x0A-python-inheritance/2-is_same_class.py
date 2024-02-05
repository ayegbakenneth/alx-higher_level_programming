i!/usr/bin/python3
"""Class-checking function."""

def is_same_class(obj, a_class):
    """This access if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to confirm
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
