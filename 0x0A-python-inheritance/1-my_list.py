#!/usr/bin/python3
"""Inherited list class definations."""

class MyList(list):
    """Sorted built-in list class implementation."""

    def print_sorted(self):
        """This Prints a list in a sorted order."""
        print(sorted(self))
