"""

Using the unittest framework, create a TestJoinMethod class that inherits
from the unittest.TestCase class and implements the following three tests:

test_join_with_space()

test that checks if the code ' '.join(['Python', '3.8'])
returns a list 'Python 3.8'


test_join_with_comma()

test that checks if the code ','.join(['open', 'high', 'low', 'close'])
returns a list 'open,high,low,close'


test_join_with_new_line_char()

test that checks if the code '\n'.join(['open', 'high', 'low', 'close'])
returns a list 'open\nhigh\nlow\nclose'



You only need to define the class and the appropriate tests.
During the solution verification, the tests are run and in case of any errors,
the test report will be printed to the console.

"""

import unittest


class TestJoinMethod(unittest.TestCase):

    def test_join_with_space(self):
        current = ' '.join(['Python', '3.8'])
        expected = 'Python 3.8'

        self.assertEqual(current, expected)

    def test_join_with_comma(self):
        current = ','.join(['open', 'high', 'low', 'close'])
        expected = 'open,high,low,close'

        self.assertEqual(current, expected)

    def test_join_with_new_line_char(self):
        current = '\n'.join(['open', 'high', 'low', 'close'])
        expected = 'open\nhigh\nlow\nclose'

        self.assertEqual(current, expected)


if __name__ == '__main__':
    unittest.main()