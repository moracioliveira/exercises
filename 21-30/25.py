"""
Suppose you have a function called calculate_average()
that takes a list of numbers as input and returns
the average of those numbers.
Your task is to write test cases for this function using unittest.

Here's an example implementation of the calculate_average() function:

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

Using the unittest framework create the unit test class
named TestCalculateAverage and implement the following test cases:

test_calculate_average_valid_input() - 3 different assertions
test_calculate_average_empty_input() - 1 assertion
test_calculate_average_invalid_input() - 3 different assertions

Choose the input data for the tests according
to the description of the test methods.
You should use a total of 7 assertion methods.
"""
import unittest


class TestCalculateAverage(unittest.TestCase):

    def test_calculate_average_valid_input(self):
        self.assertEqual(calculate_average([5,6,7,8]), 6.5)
        self.assertEqual(calculate_average([10,11,12,13]), 11.5)
        self.assertEqual(calculate_average([1,2,3,4]), 2.5)

    def test_calculate_average_empty_input(self):
        self.assertEqual(calculate_average([]), None)

    def test_calculate_average_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate_average(['w','y','u','s'])
        self.assertRaises(TypeError, calculate_average, ['e','g','k','q'])
        self.assertRaises(TypeError, calculate_average, ['l','o','m','v'])

if __name__ == '__main__':
    unittest.main()