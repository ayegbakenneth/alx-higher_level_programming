#!/usr/bin/python3
# 6-from_json_string.py
"""Function that shows json data interchange."""
import json


def from_json_string(my_str):
    """Return the Python object implementation of a JSON file."""
    return json.loads(my_str)
