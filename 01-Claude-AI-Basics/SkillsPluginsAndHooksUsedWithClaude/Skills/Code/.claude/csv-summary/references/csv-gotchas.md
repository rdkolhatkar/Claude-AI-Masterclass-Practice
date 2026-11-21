# CSV Gotchas — extra reference

This file is only read when `summarize.py` fails or the output looks wrong. It covers the two most common CSV problems for beginners.

## Problem 1 — Wrong encoding (UnicodeDecodeError)

**Symptom:** The script crashes with `UnicodeDecodeError`, or you see strange characters like `Ã©` where `é` should be.

**Cause:** The file is not UTF-8. Files saved from older versions of Excel on Windows are often `cp1252` or `latin-1` instead.

**Fix:** Temporarily change this line inside `summarize.py`:

```python
with open(path, "r", encoding="utf-8", newline="") as f:
```

to:

```python
with open(path, "r", encoding="latin-1", newline="") as f:
```

Then run the script again. Tell the user which encoding worked so they can re-save the file as UTF-8 later.

## Problem 2 — Wrong delimiter (one column when there should be many)

**Symptom:** The script reports only 1 column even though the file clearly has many values per row.

**Cause:** The file uses a semicolon (`;`) or tab as the separator instead of a comma. Semicolon-separated files are common in European exports.

**Fix:** Open the first line of the CSV in VS Code. If you see semicolons between values, change this line inside `summarize.py`:

```python
reader = csv.reader(f)
```

to:

```python
reader = csv.reader(f, delimiter=";")
```

Then run the script again.

## When in doubt

Open the file in VS Code and look at the first few lines with your own eyes. 90% of CSV problems become obvious in 10 seconds.
