import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    # ARRANGE, ACT and ASSERT <- General template

    def test_sum(self):
        # ARRANGE
        testCal = Calculator(8,2)
        # ACT & ASSERT
        self.assertEqual(testCalc.get_sum(), 10, "The sum is wrong")

    def test_subtract(self):
        # ARRANGE
        testCal = Calculator(8,2)
        # ACT & ASSERT
        self.assertEqual(testCalc.get_subtract(), 6, "The sum is wrong")

    def test_multiply(self):
        # ARRANGE
        testCal = Calculator(8,2)
        # ACT & ASSERT
        self.assertEqual(testCalc.get_multiply(), 16, "The sum is wrong")

    def test_division(self):
        # ARRANGE
        testCal = Calculator(8,2)
        # ACT & ASSERT
        self.assertEqual(testCalc.get_division(), 4, "The sum is wrong")

    # def tearDown(self):
    #     pass

if __name__ = "__main__":
    unittest.main()