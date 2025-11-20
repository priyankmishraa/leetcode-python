# test_two_sum.py
import unittest
from two_sum import twoSum

class TestTwoSum(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self):
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])

    def test_example3(self):
        self.assertEqual(twoSum([3, 3], 6), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(twoSum([-1, -2, -3, -4], -6), [1, 3])

if __name__ == "__main__":
    unittest.main()
