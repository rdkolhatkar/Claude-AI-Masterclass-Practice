# Change the Directory to the location of this file before running it. => cd 01-Claude-AI-Basics/BasicProjectUsingClaudeCLI/Python
# To Run this file, use the command: python myApp.py
# myApp.py — Basic Calculator (with divide-by-zero fix)
# Based on app.py, which is left unchanged.


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the result of subtracting b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Basic Calculator")
    print("----------------")
    print(f"10 + 5  = {add(10, 5)}")
    print(f"10 - 5  = {subtract(10, 5)}")
    print(f"10 * 5  = {multiply(10, 5)}")
    print(f"10 / 5  = {divide(10, 5)}")

    try:
        print(f"10 / 0  = {divide(10, 0)}")
    except ValueError as error:
        print(f"10 / 0  = Error: {error}")
