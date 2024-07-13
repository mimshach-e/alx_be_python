# Task: Write Unit Tests in test_simple_calculator.py
# Import the Necessary Modules:
import unittest
from simple_calculator import SimpleCalculator

# Define a Test Class:
class TestSimpleCalculator(unittest.TestCase):

# Write Test Methods:
    def test_add(self):
        # est for edge cases
        try:
          # Use Assertions to Verify Results:
          self.assertEqual(SimpleCalculator(3, 5), 8)
          self.assertEqual(SimpleCalculator(-1, 5), 4)
          self.assertEqual(SimpleCalculator(0, 6), 6)
          self.assertEqual(SimpleCalculator('a', 4))
          self.assertEqual(SimpleCalculator(None))
        except TypeError as t:
           print(t)

    def test_subtract(self):
       try:
         
         self.assertEqual(SimpleCalculator(4, 1),3)
         self.assertEqual(SimpleCalculator(-3, -3), 0)
         self.assertEqual(SimpleCalculator(5, -5), 10)
         self.assertEqual(SimpleCalculator(10, 0), 10)
         self.assertEqual(SimpleCalculator(4, 'b'))
         self.assertEqual(SimpleCalculator(None))
       except TypeError as tt:
          print(tt)

    def test_multiply(self):
       try:
          self.assertEqual(SimpleCalculator(0, 5), 0)
          self.assertEqual(SimpleCalculator(5, -2), -10)
          self.assertEqual(SimpleCalculator(3, 2), 6)
          self.assertEqual(SimpleCalculator(-4, -4), 16)
          self.assertEqual(SimpleCalculator("c", 4))
          self.assertEqual(SimpleCalculator(None))
       except TypeError as err:
          print(err)

    def test_divide(self):
       try:
          self.assertEqual(SimpleCalculator(10, 2), 5)
          self.assertEqual(SimpleCalculator(0, 3), 0)
          self.assertEqual(SimpleCalculator(4, 0))
          self.assertEqual(SimpleCalculator(10, -5), -2)
          self.assertEqual(SimpleCalculator("d", 10))
          self.assertEqual(SimpleCalculator(None))
       except ZeroDivisionError as zer:
          print(zer)
       except TypeError as te:
          print(te)     

if __name__ == "__main__":
 unittest()




       
       
