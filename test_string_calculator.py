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
    
    def test_add_two_numbers(self):
        calculator = StringCalculator()
        result = calculator.add("1,5")
        self.assertEqual(result, 6)
    
    def test_add_numbers_with_newlines(self):
        calculator = StringCalculator()
        result = calculator.add("1\n2,3")
        self.assertEqual(result, 6)
    
    def test_add_numbers_with_custom_delimiter(self):
        calculator = StringCalculator()
        result = calculator.add("//;\n1;2")
        self.assertEqual(result, 3)
    
    def test_add_negative_numbers(self):
        calculator = StringCalculator()
        with self.assertRaises(ValueError):
            calculator.add("1,-2,3,-4")
    
    def test_ignore_numbers_above_1000(self):
        calculator = StringCalculator()
        result = calculator.add("2,1001")
        self.assertEqual(result, 2)
    
    def test_single_delimiter_long_length():
        calculator = StringCalculator()
        result = calculator.add("//[;;]\n1;;2")
        assert result == 3

if __name__ == '__main__':
    unittest.main()
