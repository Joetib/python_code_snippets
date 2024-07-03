# Use the built-in unittest module for unit testing in Python
import unittest

# Create a test case class that inherits from unittest.TestCase
class TestMyCode(unittest.TestCase):

    # Define test methods starting with 'test_'
    def test_addition(self):
        self.assertEqual(2 + 2, 4)  # Check if 2 + 2 equals 4

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)  # Check if 5 - 3 equals 2

    def test_multiplication(self):
        self.assertEqual(3 * 4, 12)  # Check if 3 * 4 equals 12

# Run the tests when the script is executed
if __name__ == '__main__':
    unittest.main()

# Output
# ..
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
#
# OK
# Please Like and Subscribe