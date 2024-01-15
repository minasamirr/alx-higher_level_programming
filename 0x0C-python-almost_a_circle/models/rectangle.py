#!/usr/bin/python3
"""Module for the Rectangle class"""


class Rectangle:
    """The Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): x-coordinate of the rectangle (default is 0)
            y (int): y-coordinate of the rectangle (default is 0)
            id (int): Identifier for the rectangle (default is None)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle using '#' characters"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """String representation of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        Update attributes with provided arguments or key-worded arguments
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the Rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
