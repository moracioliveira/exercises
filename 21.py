"""
Using the unittest framework create three classes named:
TestLstripMethod, TestStripMethod and TestRstripMethod
that inherit from the unittest.TestCase class.
Then add two test methods to each class, testing the behavior of the methods appropriately:

str.lstrip()
str.strip()
str.rstrip()

Choose appropriate names for the test cases and test methods at your discretion.

"""
import unittest


class TestLstripMethod(unittest.TestCase):

    def test_removes_first_three(self):
        assert '     carwash'.lstrip() == 'carwash'

    def test_removes_additional_first_three(self):
        assert '    laundry'.lstrip() == 'laundry'

class TestStripMethod(unittest.TestCase):

    def test_remove_selected(self):
        assert '   carwash   '.strip() == 'carwash'

    def test_remove_additional_selected(self):
        assert '    laundry      '.strip() == 'laundry'

class TestRstripMethod(unittest.TestCase):

    def test_removes_last_three(self):
        assert 'carwash     '.rstrip() == 'carwash'

    def test_removes_additional_last_three(self):
        assert 'laundry      '.rstrip() == 'laundry'


if __name__ == '__main__':
    unittest.main()