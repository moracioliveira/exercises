"""
Suppose you have the Rectangle class with the area() method:

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._validate_params(width, height)
        self.width = width
        self.height = height

    def _validate_params(self, width: float, height: float) -> None:
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Width must be a positive number")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Height must be a positive number")

    def area(self) -> float:
        return self.width * self.height


Create the unit test class named TestRectangle and define the test cases:

test_area_with_nonzero_dimensions()
test_area_with_zero_dimensions()
test_area_with_negative_width()
test_area_with_negative_height()
test_area_with_float_dimensions()
test_area_with_large_dimensions()

In the test_area() method tests the area() method
of the Rectangle class by creating a new instance of the class
with three different width and height values, calling the area() method,
and checking that the return value matches the expected result using the assertEqual() method.
"""
import unittest


class TestRectangle(unittest.TestCase):

    def test_area_with_nonzero_dimensions(self):
        self.assertTrue(isinstance(Rectangle(2.0,3.0).area(), float))

    def test_area_with_zero_dimensions(self):
        self.assertTrue(isinstance(Rectangle(0, 0).area(), int))

    def test_area_with_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 5).area()

    def test_area_with_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -5).area()

    def test_area_with_float_dimensions(self):
        self.assertTrue(isinstance(Rectangle(2.5, 3.5).area(), float))

    def test_area_with_large_dimensions(self):
        self.assertTrue(isinstance(Rectangle(100.0, 300.0).area(), float))

if __name__ == '__main__':
    unittest.main()