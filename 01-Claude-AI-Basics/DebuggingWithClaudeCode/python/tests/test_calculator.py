import unittest

from calculator import (
    apply_discount,
    calculate_daily_budget,
    calculate_total_cost,
    cost_per_person,
    is_within_budget,
)


class TestCalculateTotalCost(unittest.TestCase):
    def test_adds_all_components(self):
        self.assertEqual(calculate_total_cost(500, 300, 150), 950)


class TestCostPerPerson(unittest.TestCase):
    def test_divides_total_by_people(self):
        self.assertEqual(cost_per_person(900, 3), 300)

    def test_zero_people_raises_value_error(self):
        with self.assertRaises(ValueError):
            cost_per_person(900, 0)


class TestIsWithinBudget(unittest.TestCase):
    def test_under_budget_is_true(self):
        self.assertTrue(is_within_budget(950, 1200))

    def test_over_budget_is_false(self):
        self.assertFalse(is_within_budget(1500, 1200))


class TestApplyDiscount(unittest.TestCase):
    def test_returns_discounted_float(self):
        result = apply_discount(1000, 10)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 900.0)


class TestCalculateDailyBudget(unittest.TestCase):
    def test_returns_one_budget_per_day(self):
        daily = calculate_daily_budget(900, 5)
        self.assertEqual(len(daily), 5)
        self.assertEqual(daily, [180.0] * 5)


if __name__ == "__main__":
    unittest.main()
