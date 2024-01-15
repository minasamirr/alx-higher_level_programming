#!/usr/bin/python3
"""Unit test class Rectangle"""
import unittest
import json
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""
    

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 2)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -2)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_negative_width_and_height(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, -2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "invalid")

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 2, -1)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 2, 1, -1)

    def test_area_calculation(self):
        r = Rectangle(5, 2)
        self.assertEqual(r.area(), 10)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 2, "invalid")

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 2, 1, "invalid")

    def test_area_calculation_after_resize(self):
        r = Rectangle(5, 2)
        r.width = 3
        r.height = 4
        self.assertEqual(r.area(), 12)

    def test_display_output(self):
        r = Rectangle(2, 3)
        with self.assertLogs() as logs:
            r.display()
        self.assertEqual(logs.output, ['OO', 'OO', 'OO'])
