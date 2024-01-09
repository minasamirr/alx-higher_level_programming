#!/usr/bin/python3
"""
Module for writing an object to a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function to write an object to a text file using JSON representation.

    Parameters:
    - my_obj: The object to be saved to the file.
    - filename (str): The name of the file to save the object.

    Returns:
    - None
    """
    # Open the file in write mode with UTF-8 encoding using 'with' statement
    with open(filename, mode='w', encoding='utf-8') as file:
        # Serialize the object to JSON and write to the file
        json.dump(my_obj, file)
