# string_utils.py (including the functions and tests)

import unittest

# Functions to test
def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def is_capitalized(s):
    return s[0].isupper()

# Test case class for testing the string utility functions
class TestStringUtils(unittest.TestCase):

    # Test reverse_string function
    def test_reverse_string(self):
        result = reverse_string("hello")
        self.assertEqual(result, "olleh")  # Verify that "hello" is reversed to "olleh"
    
    # Test capitalize_string function
    def test_capitalize_string(self):
        result = capitalize_string("hello")
        self.assertEqual(result, "Hello")  # Verify that "hello" is capitalized to "Hello"
    
    # Test is_capitalized function
    def test_is_capitalized(self):
        result = is_capitalized("Hello")
        self.assertTrue(result)  # Verify that "Hello" is capitalized
        
        result = is_capitalized("hello")
        self.assertFalse(result)  # Verify that "hello" is not capitalized

# Run the tests
if __name__ == '__main__':
    unittest.main()
