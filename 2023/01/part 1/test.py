import unittest
from code import value_of_digits, first_and_last_digits

class Test(unittest.TestCase):
    def test_first_and_last_digits(self):
        self.assertEqual(('1', '2'), first_and_last_digits('1abc2'))
        self.assertEqual(('3', '8'), first_and_last_digits('pqr3stu8vwx'))
        self.assertEqual(('1', '5'), first_and_last_digits('a1b2c3d4e5f'))
        self.assertEqual(('7', '7'), first_and_last_digits('treb7uchet'))

    def test_value_of_digits(self):
        self.assertEqual(12, value_of_digits(('1', '2')))
        self.assertEqual(38, value_of_digits(('3', '8')))
        self.assertEqual(15, value_of_digits(('1', '5')))
        self.assertEqual(77, value_of_digits(('7', '7')))
