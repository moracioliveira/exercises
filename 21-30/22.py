"""
Suppose you have the StringReverser class with the reverse method:

class StringReverser:
    def reverse(self, string):
        return string[::-1]

Create the unit test class named TestStringReverser
and define the test cases. The test_reverse() method
should test the reverse() method of the StringReverser class
by creating a new instance of the class,
calling the reverse() method with different strings,
and checking that the return value matches the expected result using the assertEqual() method.

Test the reverse() method with three different strings:

"hello"
"12345"

"" (empty string)

The expected results are "olleh", "54321", and "", respectively.
"""
import unittest

class StringReverser:
    def reverse(self, string):
        return string[::-1]


# Enter your solution here
class TestStringReverser(unittest.TestCase):

    def test_reverse(self):

        self.assertEqual(StringReverser().reverse("hello"), "olleh")
        self.assertEqual(StringReverser().reverse("12345"), "54321")
        self.assertEqual(StringReverser().reverse(""), "")

if __name__ == '__main__':
    unittest.main()
