import unittest


# The class that contains the methods to test
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


# The test class
class TestCalculator(unittest.TestCase):
    # This method is run before each test method
    def setUp(self):
        self.calculator = Calculator()

    # Test the add method of the Calculator class
    def test_add(self):
        result = self.calculator.add(3, 4)
        self.assertEqual(result, 7)

    # Test the subtract method of the Calculator class
    def test_subtract(self):
        result = self.calculator.subtract(8, 3)
        self.assertEqual(result, 5)


# Run the tests
if __name__ == "__main__":
    unittest.main()
