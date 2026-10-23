# CLAUDE.md — Trip Cost Calculator

## Project Overview
A command-line Trip Cost Calculator written in Python.
Users enter trip details and the app calculates total costs,
cost per person, and a formatted trip summary.

## Coding Standards
- Use Python 3.10+
- Follow PEP 8 style guidelines
- Add a docstring to every function
- Use type hints for all function parameters and return values
- Use f-strings for all string formatting
- Never suppress exceptions silently — always show a clear error message

## Project Structure
```
trip_cost_calculator/
├── CLAUDE.md          ← You are here (AI instruction file)
├── calculator.py      ← Main calculation logic (has bugs — needs fixing)
└── tests/
    └── test_calculator.py  ← Unit tests
```

## Testing
- Use Python's built-in unittest module
- Run tests with: python -m unittest discover
- Every fixed function must have at least one test

## Off-Limits
- Do NOT modify CLAUDE.md unless explicitly asked
- Do NOT delete any file without confirmation

## Notes for Claude Code
- Always read this file and calculator.py before making any changes
- Explain what each bug is before fixing it
- Fix one bug at a time so the student can follow along
- After fixing all bugs, confirm the app runs without errors
