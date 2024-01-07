#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize the new text
    new_text = ""
    
    # Iterate through each character in the text
    for char in text:
        new_text += char
        if char in ['.', '?', ':']:
            new_text += '\n\n'

    # Print the modified text
    print(new_text, end='')
