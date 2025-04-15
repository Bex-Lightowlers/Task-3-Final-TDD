import unittest
from leap_year import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test_tests_work(self):
        self.assertTrue(2+2,4)

    def test_true_leap_year(self):
        self.assertTrue(is_leap_year(2000)) #is a leap year
        self.assertTrue(is_leap_year(2004))

    def test_false_leap_year(self):
        self.assertFalse(is_leap_year(2001)) #is not a leap year 

if __name__=='__main__':
    unittest.main()