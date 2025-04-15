import unittest
from leap_year import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test_tests_work(self):
        self.assertTrue(2+2,4)

    def test_true_leap_year(self):
        self.assertTrue(is_leap_year(2000)) #is a leap year
        self.assertTrue(is_leap_year(2003))

if __name__=='__main__':
    unittest.main()