#!/usr/bin/python3
"""Introduce a student class."""


class Student:
    """Implementation of a student class."""

    def __init__(self, first_name, last_name, age):
        """New Student initialisation.

        Args:
            First_name (str): First name of student.
            Last_name (str): Last name of student.
            Age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
