#!/usr/bin/python3
"""A student class defination."""


class Student:
    """Implementation of the student class."""

    def __init__(self, first_name, last_name, age):
        """New Student initialisation.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A dictionary implementation of the Student."""
        return self.__dict__
