import unittest
from unittest import TestCase
from price_discount import discount

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [58, 32, 90]
        expected_discount = 32
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_four_prices(self):
        prices = [93, 35, 43, 6]
        expected_discount = 6
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_two_prices(self):
        prices = [32, 9]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_zero_prices(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))
    
    def test_list_of_six_prices(self):
        prices = [67, 67, 50, 35, 17, 93]
        expected_discount = 17
        self.assertEqual(expected_discount, discount(prices))

    def test_string_prices(self):
        prices = ['ten', 'four', 'twenty']
        with self.assertRaises(Exception):
            discount(prices)

    def test_negative_prices(self):
        prices = [-36, 4, 15]
        with self.assertRaises(Exception):
            discount(prices)

    def test_floating_point_prices(self):
        prices = [32.5, 72.2, 7.8]
        expected_discount = 7.8
        self.assertEqual(expected_discount, discount(prices))

    def test_duplicate_prices(self):
        prices = [10, 10, 20]
        expected_discount = 10
        self.assertEqual(expected_discount, discount(prices))
    
    def test_not_array(self):
        prices = 10
        with self.assertRaises(Exception):
            discount(prices)

if __name__ == '__main__':
    unittest.main()
