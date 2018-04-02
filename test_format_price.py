import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):
    def test_big_number(self):
        self.assertEqual(format_price(123456789123), '123 456 789 123')

    def test_decimals(self):
        self.assertEqual(format_price(123456.123), '123 456.123')

    def test_zero_decimals(self):
        self.assertEqual(format_price(123456.0), '123 456')

    def test_minus(self):
        self.assertEqual(format_price(-123456), '-123 456')

    def test_string_arg(self):
        self.assertEqual(format_price('string'), None)


if __name__ == '__main__':
    unittest.main()
