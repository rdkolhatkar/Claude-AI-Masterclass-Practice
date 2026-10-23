# calculator.py — Trip Cost Calculator
# This file contains intentional bugs for the Lecture 6.4 debugging demo.
# Do NOT fix these manually — use Claude Code in VS Code!

import math


# ── Bug 1: Wrong operator — uses multiplication instead of addition ──────────
def calculate_total_cost(flight: float, hotel: float, food: float) -> float:
    """Calculate the total cost of a trip from individual components."""
    return flight * hotel * food          # BUG: should be flight + hotel + food


# ── Bug 2: Division by zero — no check when num_people is 0 ─────────────────
def cost_per_person(total_cost: float, num_people: int) -> float:
    """Calculate the cost per person for a group trip."""
    return total_cost / num_people        # BUG: crashes if num_people is 0


# ── Bug 3: Wrong variable name — uses 'budgt' instead of 'budget' ───────────
def is_within_budget(total_cost: float, budget: float) -> bool:
    """Return True if total cost is within the given budget."""
    return total_cost <= budgt            # BUG: NameError — 'budgt' is not defined


# ── Bug 4: Wrong return type — returns a string instead of a float ──────────
def apply_discount(total_cost: float, discount_percent: float) -> float:
    """Apply a percentage discount and return the discounted total."""
    discounted = total_cost - (total_cost * discount_percent / 100)
    return str(discounted)               # BUG: returns str, should return float


# ── Bug 5: Off-by-one — loop misses the last day ────────────────────────────
def calculate_daily_budget(total_budget: float, num_days: int) -> list:
    """Return a list of equal daily budgets across the trip duration."""
    daily = total_budget / num_days
    return [daily for _ in range(num_days - 1)]   # BUG: should be range(num_days)


# ── Main runner ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Trip Cost Calculator")
    print("====================")

    total = calculate_total_cost(500, 300, 150)
    print(f"Total trip cost:    ${total}")

    per_person = cost_per_person(total, 3)
    print(f"Cost per person:    ${per_person:.2f}")

    within = is_within_budget(total, 1200)
    print(f"Within budget:      {within}")

    discounted = apply_discount(total, 10)
    print(f"After 10% discount: ${discounted:.2f}")

    daily = calculate_daily_budget(900, 5)
    print(f"Daily budgets:      {daily}")
    print(f"Days covered:       {len(daily)}")
