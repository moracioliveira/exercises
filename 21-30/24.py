"""
Suppose you have the TemperatureConverter class with the celsius_to_fahrenheit method:

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32

Create the unit test class named TestTemperatureConverter and define the test cases.

In the test_celsius_to_fahrenheit() method tests the celsius_to_fahrenheit() static method
of the TemperatureConverter class by creating a new instance of the class,
calling the celsius_to_fahrenheit() method with three different temperature values in Celsius,
and checking that the return value matches the expected result using the assertAlmostEqual() method.
"""
import unittest

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConverter().celsius_to_fahrenheit(40), 108, delta=5.0)
        self.assertAlmostEqual(TemperatureConverter().celsius_to_fahrenheit(30), 90, delta=5.0)
        self.assertAlmostEqual(TemperatureConverter().celsius_to_fahrenheit(20), 70, delta=5.0)

if __name__ == '__main__':
    unittest.main()