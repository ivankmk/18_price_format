import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_big_number(self):
        test_value1 = 123456789123
        self.assertEqual(format_price(test_value1), '123 456 789 123')

    def test_decimals(self):
        test_value2 = 123456.123
        self.assertEqual(format_price(test_value2), '123 456.123')

    def test_zero_decimals(self):
        test_value3 = 123456.0
        self.assertEqual(format_price(test_value3), '123 456')

    def test_minus(self):
        test_value4 = -123456
        self.assertEqual(format_price(test_value4), '-123 456')

    def test_string_arg(self):
        test_value5 = 'string'
        self.assertEqual(format_price(test_value5), None)


if __name__ == '__main__':
    unittest.main()
