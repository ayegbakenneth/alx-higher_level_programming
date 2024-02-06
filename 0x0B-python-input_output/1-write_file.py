#!/usr/bin/python3
"""This module defines a function that write into file."""

def write_file(filename="", text=""):
    """Function that write a string to a text file.

    Args:
        filename (str): Name of the file.
        text (str): Text written to the file.
    Returns:
        Total characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
