#!/usr/bin/python3
"""Module for the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): x-coordinate of the rectangle (default is 0)
            y (int): y-coordinate of the rectangle (default is 0)
            id (int): Identifier for the rectangle (default is None)
        """
        super().__init__(id)  # Call the super class with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance using '#' characters"""
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """String representation of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )


if __name__ == "__main__":
    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)