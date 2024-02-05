#!/usr/bin/python3
"""This implement a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a square subclass."""

    def __init__(self, size):
        """a new square initialisation.

        Args:
            size (int): Size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size