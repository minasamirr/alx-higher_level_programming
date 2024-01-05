#!/usr/bin/python3
"""
Define a class LockedClass
"""


class LockedClass:
    """
    Use __slots__ to allow only 'first_name' as an instance attribute
    """
    __slots__ = ['first_name']
