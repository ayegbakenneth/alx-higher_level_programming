#!/usr/bin/python3
"""How to implement a text file-reading function."""


def read_file(filename=""):
    """This function Print contents of a text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
