# (minimum score, grade, status), checked from highest to lowest.
GRADE_BANDS = [
    (90, "A", "Excellent"),
    (80, "B", "Good"),
    (70, "C", "Average"),
    (60, "D", "Below Average"),
]
FAILING_GRADE = ("F", "Failing")


def grade_and_status(score):
    """Return the (grade, status) pair for a numeric score."""
    for minimum, grade, status in GRADE_BANDS:
        if score >= minimum:
            return grade, status
    return FAILING_GRADE


def calc(score):
    """Print the score, grade and status, then return the grade."""
    grade, status = grade_and_status(score)
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")
    return grade


def calc2(score):
    """Return the letter grade for a score without printing anything."""
    grade, _ = grade_and_status(score)
    return grade


calc(85)
calc(72)
print(calc2(95))
