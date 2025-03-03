# unexpected.py

import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)

def divide(a, b):
    return a / b


# Test case class for edge cases
class TestUnexpected(unittest.TestCase):

    # Test get_sqrt() for valid inputs
    def test_get_sqrt_valid(self):
        result = get_sqrt(144)
        self.assertEqual(result, 12)  # Verify that sqrt(144) is 12
    
    # Test get_sqrt() for negative input
    def test_get_sqrt_negative(self):
        with self.assertRaises(ValueError):  # sqrt of negative number should raise ValueError
            get_sqrt(-9)

    # Test divide() for valid inputs
    def test_divide_valid(self):
        result = divide(144, 12)
        self.assertEqual(result, 12)  # Verify that 144 / 12 is 12
    
    # Test divide() for division by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):  # Dividing by zero should raise ZeroDivisionError
            divide(144, 0)

# Run the tests
if __name__ == '__main__':
    unittest.main()
