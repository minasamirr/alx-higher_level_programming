#!/usr/bin/python3
"""
Module for defining a Student class.
"""


class Student:
    """
    Student class with public instance attributes and a to_json method.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs (list): A list of strings containing attribute names to
        be retrieved.
                       If None, all attributes must be retrieved.

        Returns:
        - dict: A dictionary representation of the Student instance.
        """
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__

        return {attr: getattr(self, attr, None) for attr in attrs}
