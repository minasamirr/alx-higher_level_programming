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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
        - dict: A dictionary representation of the Student instance.
        """
        # Get the attributes of the object
        attributes = self.__dict__

        # Convert any nested objects to dictionaries recursively
        for key, value in attributes.items():
            if hasattr(value, '__dict__'):
                attributes[key] = class_to_json(value)

        return attributes
