# CLAUDE.md — Travel Report Generator

## Project Overview
A command-line Travel Report Generator written in Python.
It processes a list of trips and prints cost summaries,
travel statistics, and budget warnings.

## Target Coding Standards (after refactoring)
- Use Python 3.10+
- Follow PEP 8 style guidelines
- Add a docstring to every function
- Use type hints for all function parameters and return values
- Use f-strings for all string formatting
- Keep functions small — one task per function (max ~15 lines)
- No global variables — pass data as function arguments
- Use UPPER_CASE for constants (e.g. WARNING_THRESHOLD = 0.9)
- Use consistent snake_case naming for all variables and functions
- No magic numbers — replace with named constants

## Project Structure
```
travel_report/
├── CLAUDE.md          ← You are here
├── report.py          ← Main file (needs heavy refactoring)
└── tests/
    └── test_report.py ← Unit tests (to be created after refactoring)
```

## Testing
- Use Python's built-in unittest module
- Run tests with: python -m unittest discover

## Off-Limits
- Do NOT modify CLAUDE.md
- The logic of the program must produce the same output after refactoring
  (refactoring changes structure, not behaviour)
