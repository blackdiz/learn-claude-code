"""Unit tests for utils module.

This module contains tests for the utility functions in my_package.utils.
"""

import unittest
from my_package.utils import add, multiply


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""

    def test_add_integers(self) -> None:
        """Test adding two integers."""
        self.assertEqual(add(2, 3), 5)

    def test_add_floats(self) -> None:
        """Test adding two floats."""
        self.assertAlmostEqual(add(2.5, 3.7), 6.2)

    def test_add_negative(self) -> None:
        """Test adding with negative numbers."""
        self.assertEqual(add(-5, 3), -2)

    def test_multiply_integers(self) -> None:
        """Test multiplying two integers."""
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_floats(self) -> None:
        """Test multiplying two floats."""
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)

    def test_multiply_negative(self) -> None:
        """Test multiplying with negative numbers."""
        self.assertEqual(multiply(-3, 4), -12)

    def test_multiply_zero(self) -> None:
        """Test multiplying by zero."""
        self.assertEqual(multiply(5, 0), 0)


if __name__ == "__main__":
    unittest.main()
