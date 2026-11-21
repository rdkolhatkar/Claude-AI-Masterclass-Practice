"""
summarize.py - quick look at a CSV file.

Usage:
    python summarize.py <path-to-csv>

Prints:
    - File name
    - Number of rows and columns
    - Column names
    - First 3 data rows
"""

import argparse
import csv
import itertools
import os
import sys


def summarize(path):
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if headers is None:
                print("ERROR: file is empty")
                sys.exit(1)
            # Stream the rows: keep only the first 3, count the rest.
            first_rows = list(itertools.islice(reader, 3))
            row_count = len(first_rows) + sum(1 for _ in reader)
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}")
        sys.exit(1)

    print(f"File:    {os.path.basename(path)}")
    print(f"Rows:    {row_count}")
    print(f"Columns: {len(headers)}")
    print()

    print("Column names:")
    for name in headers:
        print(f"  - {name}")
    print()

    print("First 3 rows:")
    for row in first_rows:
        print(f"  {', '.join(row)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quick look at a CSV file.")
    parser.add_argument("path", help="path to the CSV file")
    summarize(parser.parse_args().path)
