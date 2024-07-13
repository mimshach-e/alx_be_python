# Task: Write Unit Tests in test_simple_calculator.py
# Import the Necessary Modules:
import unittest
from simple_calculator import SimpleCalculator

# Define a Test Class:
class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

# Write Test Methods:
    def test_addition(self):
        # est for edge cases
        try:
          # Use Assertions to Verify Results:
          self.assertEqual(self.calc.add(3, 5), 8)
          self.assertEqual(self.calc.add(-1, 5), 4)
          self.assertEqual(self.calc.add(0, 6), 6)
          self.assertEqual(self.calc.add("a", 4), 9)
          self.assertEqual(self.calc.add(None))
        except TypeError as t:
           print(t)

    def test_subtraction(self):
       try:
         
         self.assertEqual(self.calc.subtract(4, 1),3)
         self.assertEqual(self.calc.subtract(-3, -3), 0)
         self.assertEqual(self.calc.subtract(5, -5), 10)
         self.assertEqual(self.calc.subtract(10, 0), 10)
         self.assertEqual(self.calc.subtract(4, "b"), 1)
         self.assertEqual(self.calc.subtract(None))
       except TypeError as tt:
          print(tt)

    def test_multiplication(self):
       try:
          self.assertEqual(self.calc.multiply(0, 5), 0)
          self.assertEqual(self.calc.multiply(5, -2), -10)
          self.assertEqual(self.calc.multiply(3, 2), 6)
          self.assertEqual(self.calc.multiply(-4, -4), 16)
          self.assertEqual(self.calc.multiply("c", 4), 8)
          self.assertEqual(self.calc.multiply(None))
       except TypeError as err:
          print(err)

    def test_division(self):
       try:
          self.assertEqual(self.calc.divide(10, 2), 5)
          self.assertEqual(self.calc.divide(0, 3), 0)
          self.assertEqual(self.calc.divide(4, 0))
          self.assertEqual(self.calc.divide(10, -5), -2)
          self.assertEqual(self.calc.divide("d", 10), 2)
          self.assertEqual(self.calc.divide(None))
       except ZeroDivisionError as zer:
          print(zer)
       except TypeError as te:
          print(te)     

if __name__ == "__main__":
 unittest()




       
       
