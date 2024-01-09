#!/usr/bin/python3
"""
Script for adding arguments to a Python list and saving them to a file.
"""

import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_item(args):
    """
    Function to add arguments to a Python list and save them to a file.

    Parameters:
    - args (list): The list of arguments.

    Returns:
    - None
    """
    filename = "add_item.json"

    # Check if the file exists, if not, create it
    if not path.exists(filename):
        save_to_json_file([], filename)

    # Load the existing list from the file
    my_list = load_from_json_file(filename)

    # Add the new arguments to the list
    my_list.extend(args)

    # Save the updated list to the file
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    # Extract command line arguments excluding the script name
    arguments = sys.argv[1:]

    # Add the arguments to the list and save to file
    add_item(arguments)
