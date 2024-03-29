#!/usr/bin/python3
"""Function that writes into a file."""


def append_write(filename="", text=""):
    """Add a string to the end of a UTF8 text file
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
