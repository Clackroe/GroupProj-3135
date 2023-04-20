import unittest
import sqlite3
from unittest.mock import Mock
from core.utils import dict_factory, calculate_cost, compare_cost, compare_mileage


class TestVehicleFunctions(unittest.TestCase):

    def setUp(self):
        # Set up a mock database connection and cursor for testing
        self.conn = Mock(spec=sqlite3.Connection)
        self.cursor = Mock(spec=sqlite3.Cursor)
        self.conn.cursor.return_value = self.cursor

    def test_dict_factory(self):
        # Test that dict_factory returns a dictionary from a row tuple
        row = ('123456', 'Honda', 'Accord', '2015', 10000)
        self.cursor.description = [('vin',), ('make',), ('model',), ('year',), ('price',)]
        result = dict_factory(self.cursor, row)
        expected = {'vin': '123456', 'make': 'Honda', 'model': 'Accord', 'year': '2015', 'price': 10000}
        self.assertEqual(result, expected)

    def test_calculate_cost(self):
        # Test that calculate_cost returns the correct total cost
        price = 10000
        tax_rate = 0.05
        result = calculate_cost(price, tax_rate)
        expected = 10500.0
        self.assertEqual(result, expected)

    def test_compare_cost(self):
        # Test that compare_cost returns the correct cheapest price
        price1 = 10000
        price2 = 12000
        result = compare_cost(price1, price2)
        expected = price1
        self.assertEqual(result, expected)

    def test_compare_mileage(self):
        # Test that compare_mileage returns the correct lowest mileage
        miles1 = 50000
        miles2 = 60000
        result = compare_mileage(miles1, miles2)
        expected = miles1
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
