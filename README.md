# Linear Solver

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-pytest-orange.svg)

A command-line tool for solving systems of linear equations from a text file. Supports multiple systems per file, detects unique, infinite, and no-solution cases, and reports variable values with color-coded output.

---

## Features

- Parses systems of linear equations from a plain text file
- Handles multiple systems in a single file
- Detects and reports one solution, no solution, or infinite solutions
- Supports any single-letter lowercase variables (`a`–`z`)
- Supports integer and decimal coefficients (e.g., `2.5x + 1.5y = 5`)
- Color-coded terminal output for easy reading
- Verbose mode (`-v`) that displays the augmented matrix before solving
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
linear-solver -v <input_file>    # verbose mode — shows augmented matrix
```

Or without installing:

```bash
python main.py <input_file>
python main.py -v <input_file>
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

Test fixtures are located in `tests/fixtures/` and include:
- `simple.txt` — single system, one solution
- `two_systems.txt` — two systems, one solution each
- `decimals.txt` — decimal coefficients
- `no_solution.txt` — contradictory system
- `infinite_solutions.txt` — underdetermined system
- `mixed.txt` — 10 systems covering all cases

---

## How It Works

1. The input file is read and split on `;` to separate systems
2. Each system is split on `,` to get individual equations
3. Equations are tokenized and parsed into coefficient dictionaries
4. An augmented matrix `[A|b]` is constructed for each system
5. The rank of `A` and `[A|b]` are compared to classify the system — this handles non-invertible matrices without calling `numpy.linalg.solve` on a singular matrix
6. If exactly one solution exists, `numpy.linalg.solve` is called
7. Results are printed for each system with color-coded output

---

## Project Structure

```Plaintext
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
        └── mixed.txt
```

---

## License

MIT — see [LICENSE](LICENSE) for details.