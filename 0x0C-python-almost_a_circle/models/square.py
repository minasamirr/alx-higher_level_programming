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
        # Call the super class with id, x, y, width, and height
        super().__init__(size, size, x, y, id)
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


if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
