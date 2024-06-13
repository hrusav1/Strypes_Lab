import math
import unittest
from hrusav_L8_T1 import BisectionError, bisection, f1, f2


class TestBisection(unittest.TestCase):
    

    
    def test_root_f1(self):
        # Update expected result based on the nature of the function
        root = bisection(1, 2, f1)
        self.assertAlmostEqual(root, 1.154, places=3)

    def test_root_f2(self):
        # Update expected result based on the nature of the function
        root = bisection(0, 2, f2)
        self.assertAlmostEqual(root, 1.678, places=3)

    def test_non_numeric_input(self):
        # Test handling of non-numeric input for interval endpoints
        with self.assertRaises(BisectionError):
            bisection("a", "b", f1)

    def test_same_signs(self):
        # Test handling of invalid intervals where the function does not change sign
        with self.assertRaises(BisectionError):
            bisection(0, 1, f1)

    def test_exact_root(self):
        # Test finding an exact root
        root = bisection(1, 2, lambda x: x - 1.5)
        self.assertAlmostEqual(root, 1.5, places=3)

    def test_root_at_interval_start(self):
        # Test root at the start of the interval
        root = bisection(0, 1, lambda x: x)
        self.assertAlmostEqual(root, 0.0, places=3)

    def test_root_at_interval_end(self):
        # Test root at the end of the interval
        root = bisection(-1, 0, lambda x: x)
        self.assertAlmostEqual(root, 0.0, places=3)

    def test_function_value_zero_at_endpoint(self):
        # Test case where the function has a zero value at one of the interval endpoints
        with self.assertRaises(BisectionError):
            bisection(0, 1, lambda x: x**2 - 1)

    def test_function_value_zero_at_midpoint(self):
        # Test when the function value is zero at the midpoint
        root = bisection(-1, 1, lambda x: x)
        self.assertAlmostEqual(root, 0.0, places=3)

    def test_invalid_interval_no_sign_change(self):
        # Test case where there's no sign change in the function within the interval
        with self.assertRaises(BisectionError):
            bisection(-2, 0, lambda x: x**2 + 1)
   
    def test_other_functions(self):
        # Test with different functions
        root = bisection(1, 3, lambda x: x**3 - 2*x**2 - 5)
        self.assertAlmostEqual(root, 2.094, places=3)

    def test_unbounded_intervals(self):
        # Test cases with unbounded intervals
        # Interval [1, +∞) for function f1
        root = bisection(1, math.inf, f1)
        self.assertAlmostEqual(root, 1.709, places=3)
        # Interval (-∞, 1] for function f1
        root = bisection(-math.inf, 1, f1)
        self.assertAlmostEqual(root, 1.709, places=3)
        # Interval (-∞, +∞) for function f1
        with self.assertRaises(BisectionError):
            bisection(-math.inf, math.inf, f1)

    def test_complex_functions(self):
        # Test cases with more complex functions
        # Function with multiple roots
        root = bisection(-2, 0, lambda x: x**3 - 2*x**2 - 4*x)
        self.assertAlmostEqual(root, -1.879, places=3)
        # Function with discontinuity
        with self.assertRaises(BisectionError):
            bisection(-2, 2, lambda x: math.sin(x) / x)


if __name__ == '__main__':
    unittest.main()
