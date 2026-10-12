# Change the Directory to the location of this file before running it. => cd 01-Claude-AI-Basics/BasicProjectUsingClaudeCLI/Python
# To Run this file, use the command: python app.py
# app.py — Basic Calculator
# This file is used across all 4 Claude Code setup demos (Lecture 6.1)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b  # Note: no handling for division by zero yet


if __name__ == "__main__":
    print("Basic Calculator")
    print("----------------")
    print(f"10 + 5  = {add(10, 5)}")
    print(f"10 - 5  = {subtract(10, 5)}")
    print(f"10 * 5  = {multiply(10, 5)}")
    print(f"10 / 5  = {divide(10, 5)}")
    print(f"10 / 0  = {divide(10, 0)}")   # This will crash!
