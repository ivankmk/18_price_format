import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_big_number(self):
        test_value1 = 123456789123
        self.assertEqual(format_price(test_value1), '123 456 789 123')

    def test_decimals(self):
        test_value2 = 123456.123
        self.assertEqual(format_price(test_value2), '123 456.12')

    def test_big_decimal(self):
        test_value3 = 123456.123123123
        self.assertEqual(format_price(test_value3), '123 456.12')

    def test_zero_decimals(self):
        test_value4 = 123456.0
        self.assertEqual(format_price(test_value4), '123 456')

    def test_a_lot_of_zeros(self):
        test_value5 = 123456.00000000000000
        self.assertEqual(format_price(test_value5), '123 456')

    def test_a_lot_of_zeros_and_negative(self):
        test_value6 = -123456.00000000000000
        self.assertEqual(format_price(test_value6), '-123 456')

    def test_minus(self):
        test_value7 = -123456
        self.assertEqual(format_price(test_value7), '-123 456')

    def test_minus_and_float(self):
        test_value8 = -123456.888
        self.assertEqual(format_price(test_value8), '-123 456.89')

    def test_string_arg(self):
        test_value9 = 'string'
        self.assertEqual(format_price(test_value9), None)

    def test_mixed_string_arg(self):
        test_value10 = '123412string'
        self.assertEqual(format_price(test_value10), None)

    def test_only_point(self):
        test_value11 = '.123'
        self.assertEqual(format_price(test_value11), '0.12')

    def test_only_point_and_zero(self):
        test_value12 = '.00000'
        self.assertEqual(format_price(test_value12), '0')

    def test_none(self):
        test_value13 = None
        self.assertEqual(format_price(test_value13), None)

    def test_list(self):
        test_value14 = [1, 2, 3]
        self.assertEqual(format_price(test_value14), None)

    def test_dict(self):
        test_value15 = {'a': 1}
        self.assertEqual(format_price(test_value15), None)


if __name__ == '__main__':
    unittest.main()
