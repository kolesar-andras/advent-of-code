import unittest
from code import value_of_digit, value_of_digits, first_and_last_digits

class Test(unittest.TestCase):
    def test_first_and_last_digits(self):
        self.assertEqual(('1', '2'), first_and_last_digits('1abc2'))
        self.assertEqual(('3', '8'), first_and_last_digits('pqr3stu8vwx'))
        self.assertEqual(('1', '5'), first_and_last_digits('a1b2c3d4e5f'))
        self.assertEqual(('7', '7'), first_and_last_digits('treb7uchet'))

        self.assertEqual(('two', 'nine'), first_and_last_digits('two1nine'))
        self.assertEqual(('eight', 'three'), first_and_last_digits('eightwothree'))
        self.assertEqual(('one', 'three'), first_and_last_digits('abcone2threexyz'))
        self.assertEqual(('two', 'four'), first_and_last_digits('xtwone3four'))
        self.assertEqual(('4', '2'), first_and_last_digits('4nineeightseven2'))
        self.assertEqual(('one', '4'), first_and_last_digits('zoneight234'))
        self.assertEqual(('7', 'six'), first_and_last_digits('7pqrstsixteen'))

        # test overlapped digit names
        self.assertEqual(('two', 'one'), first_and_last_digits('twone'))
        self.assertEqual(('eight', 'two'), first_and_last_digits('eightwo'))

    def test_value_of_digits(self):
        self.assertEqual(12, value_of_digits(('1', '2')))
        self.assertEqual(38, value_of_digits(('3', '8')))
        self.assertEqual(15, value_of_digits(('1', '5')))
        self.assertEqual(77, value_of_digits(('7', '7')))

        self.assertEqual(27, value_of_digits(('two', '7')))
        self.assertEqual(29, value_of_digits(('two', 'nine')))
        self.assertEqual(18, value_of_digits(('1', 'eight')))

    def test_value_of_digit(self):
        self.assertEqual(1, value_of_digit(('1')))
        self.assertEqual(1, value_of_digit(('one')))
        self.assertEqual(9, value_of_digit(('9')))
        self.assertEqual(9, value_of_digit(('nine')))
