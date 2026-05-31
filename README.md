# Linear Solver

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-pytest-orange.svg)

A command-line tool for solving systems of linear equations from a plain text file. Supports multiple systems per file, handles overdetermined and underdetermined systems, detects unique, infinite, and no-solution cases, and reports variable values with color-coded output.

---

## Features

- Parses systems of linear equations from a plain text file
- Handles multiple systems in a single file
- Detects and reports one solution, no solution, or infinite solutions
- Handles overdetermined systems (more equations than unknowns)
- Handles underdetermined systems (fewer equations than unknowns)
- Non-invertible/singular matrices are detected via rank comparison before solving — `numpy.linalg.solve` is never called on a singular matrix
- Supports any single-letter lowercase variables (`a`–`z`)
- Supports integer and decimal coefficients (e.g., `2.5x + 1.5y = 5`)
- Handles duplicate variables in one equation (e.g., `x + 2x + y = 3` → `3x + y = 3`)
- Handles zero coefficients (e.g., `0x + 2y = 4`)
- Filters empty systems from double semicolons or trailing semicolons
- Color-coded terminal output for easy reading
- Verbose mode (`-v`) that displays the augmented matrix before solving
- Fraction mode (`-f`) that displays solutions as exact fractions instead of decimals
- Descriptive error messages for malformed input

---

## Installation

**Requirements:** Python 3.11+, NumPy

Clone the repo and install:

```bash
git clone https://github.com/yourusername/linear-solver.git
cd linear-solver
pip install -e .
```

Or install dependencies manually and run directly:

```bash
pip install numpy
python main.py <input_file>
```

---

## Usage

```bash
linear-solver <input_file>
linear-solver -v <input_file>       # verbose — shows augmented matrix
linear-solver -f <input_file>       # fraction output — exact answers
linear-solver -v -f <input_file>    # combine flags
```

Or without installing:

```bash
python main.py <input_file>
python main.py -v -f <input_file>
```

---

## Input Format

Input is a plain text file with the following structure:

- Equations are separated by commas (`,`)
- Systems are separated by semicolons (`;`)
- Variables must be single lowercase letters
- Each term and operator must be space-separated
- Constants go on the right side of `=`
- Integer and decimal coefficients are both supported

**Example file:**

```
2x + 3y - z = 5, -x + 4y = 2, x + y + z = 6; a - b = 1, a + b = 3
```

This file contains two systems. The first has three equations and three unknowns; the second has two equations and two unknowns.

---

## Output

Standard output:

```
========================================
System 1:
  One solution:
    x =     1.2727
    y =     0.8182
----------------------------------------
System 2:
  No solution.
----------------------------------------
System 3:
  Infinite solutions.
----------------------------------------
```

Fraction output (`-f`):

```
========================================
System 1:
  One solution:
    x = 14/11
    y = 9/11
----------------------------------------
```

Verbose output (`-v`):

```
========================================
System 1:
  Augmented matrix [A|b]:
  Variables: ['x', 'y']
  [   2.0000    3.0000  |    5.0000 ]
  [  -1.0000    4.0000  |    2.0000 ]

  One solution:
    x =     1.2727
    y =     0.8182
----------------------------------------
```

**Color coding:**
- 🔵 Blue — system headers
- 🟢 Green — solutions and variable values
- 🔴 Red — no solution / infinite solutions
- ⚫ Gray — matrix output and separators

---

## Running Tests

```bash
pytest tests/ -v
```

Test fixtures are located in `tests/fixtures/` and cover:

| Fixture | Description |
|---|---|
| `simple.txt` | Single system, one solution |
| `two_systems.txt` | Two systems, one solution each |
| `decimals.txt` | Decimal coefficients |
| `no_solution.txt` | Contradictory system (singular matrix) |
| `infinite_solutions.txt` | Underdetermined system |
| `overdetermined.txt` | More equations than unknowns |
| `mixed.txt` | 10 systems covering all cases |
| `parser_edge_cases.txt` | Zero coefficients, duplicate variables, extra whitespace |
| `multi_edge_cases.txt` | Double semicolons, trailing semicolons |

---

## How It Works

1. The input file is read and split on `;` to separate systems; empty entries are filtered
2. Each system is split on `,` to get individual equations
3. Equations are tokenized and parsed into coefficient dictionaries; duplicate variables are summed
4. An augmented matrix `[A|b]` is constructed for each system; missing variables get a 0 coefficient
5. The rank of `A` and `[A|b]` are compared — this handles non-invertible matrices without ever calling `numpy.linalg.solve` on a singular matrix
6. Overdetermined systems (more equations than unknowns) use `numpy.linalg.lstsq` instead of `numpy.linalg.solve`
7. If exactly one solution exists, the appropriate solver is called
8. Results are printed for each system with color-coded output

---

## Project Structure

```
linear_solver/
├── main.py           # Entry point, CLI, and color output
├── parser.py         # File and equation parsing
├── solver.py         # Matrix construction and numpy solver
├── classifier.py     # Solution classification (one/none/infinite)
├── pyproject.toml    # Package config and CLI entry point
├── requirements.txt  # Dependencies
└── tests/
    ├── test_parser.py
    ├── test_solver.py
    ├── test_classifier.py
    └── fixtures/
        ├── simple.txt
        ├── two_systems.txt
        ├── decimals.txt
        ├── no_solution.txt
        ├── infinite_solutions.txt
        ├── overdetermined.txt
        ├── mixed.txt
        ├── parser_edge_cases.txt
        └── multi_edge_cases.txt
```

---

## License

MIT — see [LICENSE](LICENSE) for details.