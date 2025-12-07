# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Advent of Code solutions repository containing Python solutions for multiple years (2021, 2022, 2023, 2024). Each day's puzzle has two parts, typically saved as separate files (e.g., `day01_1.py` and `day01_2.py`).

## Repository Structure

```
python/
  ├── aoc/                 # Shared utilities package
  │   └── io.py           # Helper for extracting year/day from file path
  ├── y2021/, y2022/, y2023/, y2024/  # Solutions by year
  │   ├── dayXX_1.py      # Part 1 solutions
  │   ├── dayXX_2.py      # Part 2 solutions
  │   └── tests/          # Unit tests (not all years have them)
  └── setup.py            # Package setup

data/
  └── YYYY/               # Input data organized by year
      ├── inputXX.txt     # Real puzzle input
      └── testXX.txt      # Example inputs from problem statements
```

## Running Solutions

Solutions are standalone scripts that can be run directly:

```bash
# Run from within the year directory
cd python/y2024
python day01_1.py

# Or run from python directory
cd python
python -m y2024.day01_1
```

**Note:** Input file paths vary by year:
- 2021 solutions use relative paths like `../data/input01.txt`
- 2024 solutions use paths like `../../data/2024/input01.txt`

## Running Tests

Tests are written using pytest and exist for select days:

```bash
cd python

# Run all tests for a specific year
pytest y2024/tests/

# Run tests for a specific day
pytest y2024/tests/test_day21.py

# Run a specific test
pytest y2024/tests/test_day21.py::test_robot_find_shortest_numeric_pad
```

The `pytest.ini` file configures the Python path to allow imports like `from y2024.day21_1 import ...`.

## Code Patterns

### Solution Structure
Most solutions follow this pattern:
- `main(lines)` function that processes input and returns the answer
- `if __name__ == "__main__"` block that reads the input file and prints the result
- Part 2 solutions often import and reuse functions from Part 1

### The `aoc.io` Utility
The `aoc/io.py` module provides `this_year_day()` which extracts year and day numbers from the calling file's path. This is useful for dynamically constructing input file paths:

```python
from aoc.io import this_year_day
year, day = this_year_day()  # Returns (2024, 1) when called from y2024/day01_1.py
```

### Input Data Organization
- Real puzzle inputs are in `data/YYYY/inputXX.txt`
- Test/example inputs are in `data/YYYY/testXX.txt`
- Some days have multiple test files (e.g., `test18_1.txt`, `test18_2.txt`)
- Not all years have data directories yet (e.g., 2023, 2024 data directories may be missing)

## Development Workflow

When working on a new day's puzzle:
1. Create `dayXX_1.py` with the solution structure
2. Reference the appropriate input file path based on the year's convention
3. After solving Part 1, create `dayXX_2.py` (often importing from Part 1)
4. Optionally add tests in `tests/test_dayXX.py` for complex logic

When debugging:
- Check if test input files exist for the specific day
- Verify the relative path to the input file matches the year's convention
- Consider extracting complex logic into testable functions
