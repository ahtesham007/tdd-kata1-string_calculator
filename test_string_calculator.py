import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_add_empty_string(self):
        calculator = StringCalculator()
        result = calculator.add("")
        self.assertEqual(result, 0)
    
    def test_add_single_number(self):
        calculator = StringCalculator()
        result = calculator.add("1")
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
