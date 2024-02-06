#!/usr/bin/python3
"""A function that writes a Json file."""
import json


def save_to_json_file(my_obj, filename):
    """JSON representation of an object text file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
