import unittest
from src.student_code import calculate_average

class TestAverage(unittest.TestCase):
    def test_average_calculation(self):
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
