#!/usr/bin/python3
"""Implementation of rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass square."""

    def __init__(self, size):
        """A new square.

        Args:
            size (int): Size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
