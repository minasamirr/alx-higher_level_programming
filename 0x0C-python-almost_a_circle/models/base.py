#!/usr/bin/python3
"""Module for the Base class"""

class Base:
    """The base class for managing id attribute"""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id (int): An integer representing the id (default is None)
        """
        if id is not None:
            # Assign the public instance attribute id with the given value
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
