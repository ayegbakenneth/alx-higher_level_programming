#!/usr/bin/python3
"""This module defines a class Student."""


class Student:
    """Implementation of the class student."""

    def __init__(self, first_name, last_name, age):
        """A new Student initialisation."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary implementation of the Student.

        But if attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): Attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
