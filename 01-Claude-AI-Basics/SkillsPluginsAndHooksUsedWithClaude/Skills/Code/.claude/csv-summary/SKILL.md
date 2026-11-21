---
name: csv-summary
description: Use this skill whenever the user shares a CSV file or asks for a quick summary, overview, or "what's in this file" of a CSV dataset. Runs a simple Python script to show row count, column count, column names, and the first few rows.
---

# CSV Summary

## When to use
Use this skill whenever the user:
- Shares a `.csv` file and wants to understand it
- Says "summarize", "describe", "what's in this CSV", "take a look at this file"

## Files in this skill

The skill's helper script is `scripts/summarize.py`; `references/csv-gotchas.md` is read only if the script fails.

## Step 1 — Run the script

Run this command in the terminal, using the full path to the script inside this skill's folder (not a relative path):

```
python <skill-folder>/scripts/summarize.py <path-to-csv>
```

The script uses only Python's standard library (no pandas, no pip install). It prints:
- The file name
- The number of rows and columns
- The column names
- The first 3 data rows

## Step 2 — Explain the output

After running the script:
1. Show the script's output to the user in a code block.
2. Write 2 or 3 plain-English sentences explaining what the file contains.
3. End with one suggested next step, for example: "Want me to filter these orders by region?"

## Step 3 — If the script fails

If the script crashes or the output looks wrong (zero rows, one column when there should be many, garbled text), **then** read `references/csv-gotchas.md` in this same folder. It explains the two most common CSV problems and how to fix them.

Do **not** read `csv-gotchas.md` up front.

## Notes
- Use the script for the structural overview; do not rewrite it in your own Python code.
- Keep your explanation short and friendly. The user wants a quick look, not a report.
