#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Implementation of base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks a parameter as an integer.

        Args:
            name (str): Name of the parameter.
            value (int): Parameter to validate.
        Raises:
            TypeError: If not an integer.
            ValueError: value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
