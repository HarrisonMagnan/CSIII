# test_coffee_menu.py
import unittest
from coffee_menu import CoffeeMenu  # Import the CoffeeMenu class from the coffee_menu.py file

class TestCoffeeMenu(unittest.TestCase):

    # Setup method: create a new CoffeeMenu instance before each test
    def setUp(self):
        self.menu = CoffeeMenu()

    # Test method to check if getting the price of an existing item works
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('latte'), 2.75)

    # Test method to check if getting the price of a non-existing item raises a ValueError
    def test_get_price_non_existing_item(self):
        with self.assertRaises(ValueError):
            self.menu.get_price('mocha')

    # Test method to check if adding a new item works
    def test_add_item(self):
        self.menu.add_item('mocha', 3.00)
        self.assertEqual(self.menu.get_price('mocha'), 3.00)

    # Test method to check if adding an existing item raises a ValueError
    def test_add_item_existing(self):
        with self.assertRaises(ValueError):
            self.menu.add_item('latte', 3.00)

if __name__ == '__main__':
    unittest.main()
