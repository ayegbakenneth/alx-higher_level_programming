#!/usr/bin/python3
"""JSON function for data interchange."""
import json


def to_json_string(my_obj):
    """Return the JSON implementation of a string object."""
    return json.dumps(my_obj)
