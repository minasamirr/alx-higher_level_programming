#!/usr/bin/python3
"""Module for the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor

        Args:
            size (int): Size of the square
            x (int): x-coordinate of the square (default is 0)
            y (int): y-coordinate of the square (default is 0)
            id (int): Identifier for the square (default is None)
        """
        super().__init__(size, size, x, y, id)
        # Call the super class with id, x, y, width, and height
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def to_dictionary(self):
        """Return dictionary representation of the Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }


if __name__ == "__main__":
    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
