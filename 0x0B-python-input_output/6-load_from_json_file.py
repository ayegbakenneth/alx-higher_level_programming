#!/usr/bin/python3
"""Function that writes data into a Json file"""
import json


def load_from_json_file(filename):
    """Return a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
