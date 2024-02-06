#!/usr/bin/python3
"""How to implement JSON function for data interchange."""


def class_to_json(obj):
    """Return the implementation of a simple data structure of a dictionary."""
    return obj.__dict__
