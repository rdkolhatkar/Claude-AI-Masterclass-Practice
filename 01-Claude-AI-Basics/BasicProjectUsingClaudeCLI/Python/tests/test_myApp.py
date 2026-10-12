# test_myApp.py — Tests for the calculator functions in myApp.py

import unittest

from myApp import add, divide, multiply, subtract


class TestAdd(unittest.TestCase):
    """Tests for the add function."""

    def test_add_positive_numbers(self) -> None:
        """Adding two positive numbers returns their sum."""
        self.assertEqual(add(10, 5), 15)

    def test_add_negative_numbers(self) -> None:
        """Adding negative numbers works correctly."""
        self.assertEqual(add(-3, -7), -10)

    def test_add_decimals(self) -> None:
        """Adding decimals returns the expected value."""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)


class TestSubtract(unittest.TestCase):
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self) -> None:
        """Subtracting a smaller number from a larger one."""
        self.assertEqual(subtract(10, 5), 5)

    def test_subtract_gives_negative(self) -> None:
        """Subtracting a larger number gives a negative result."""
        self.assertEqual(subtract(5, 10), -5)


class TestMultiply(unittest.TestCase):
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self) -> None:
        """Multiplying two positive numbers returns their product."""
        self.assertEqual(multiply(10, 5), 50)

    def test_multiply_by_zero(self) -> None:
        """Multiplying by zero returns zero."""
        self.assertEqual(multiply(10, 0), 0)

    def test_multiply_negative_numbers(self) -> None:
        """Multiplying a negative and a positive number gives a negative."""
        self.assertEqual(multiply(-2, 3), -6)


class TestDivide(unittest.TestCase):
    """Tests for the divide function."""

    def test_divide_positive_numbers(self) -> None:
        """Dividing two numbers returns the quotient."""
        self.assertEqual(divide(10, 5), 2.0)

    def test_divide_gives_decimal(self) -> None:
        """Dividing can return a decimal result."""
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_zero_numerator(self) -> None:
        """Dividing zero by a number returns zero."""
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero_raises_error(self) -> None:
        """Dividing by zero raises a ValueError with a clear message."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
