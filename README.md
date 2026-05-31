# Linear Solver

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-pytest-orange.svg)

A command-line tool for solving systems of linear equations from a text file. Supports multiple systems per file, detects unique, infinite, and no-solution cases, and reports variable values clearly.

---

## Features

- Parses systems of linear equations from a plain text file
- Handles multiple systems in a single file
- Detects and reports one solution, no solution, or infinite solutions
- Supports any single-letter lowercase variables (`a`–`z`)
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
```

Or without installing:

```bash
python main.py <input_file>
```

---

## Input Format

Input is a plain text file with the following structure:

- Equations are separated by commas (`,`)
- Systems are separated by semicolons (`;`)
- Variables must be single lowercase letters
- Each term and operator must be space-separated
- Constants go on the right side of `=`

**Example file:**

```
2x + 3y - z = 5, -x + 4y = 2, x + y + z = 6; a - b = 1, a + b = 3
```

This file contains two systems. The first has three equations and three unknowns; the second has two equations and two unknowns.

---

## Output

```
System 1:
  One solution:
    x = 1.2727
    y = 0.8182
    z = 3.9091

System 2:
  One solution:
    a = 2.0000
    b = 1.0000
```

For unsolvable systems:

```
System 1:
  No solution.

System 2:
  Infinite solutions.
```

---

## Running Tests

```bash
pytest tests/ -v
```

---

## Project Structure

```
linear_solver/
├── main.py           # Entry point and CLI
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
        └── two_systems.txt
```

---

## How It Works

1. The input file is read and split on `;` to separate systems
2. Each system is split on `,` to get individual equations
3. Equations are tokenized and parsed into coefficient dictionaries
4. An augmented matrix `[A|b]` is constructed for each system
5. The rank of `A` and `[A|b]` are compared to classify the system
6. If exactly one solution exists, `numpy.linalg.solve` is called
7. Results are printed for each system

---

## License

MIT — see [LICENSE](LICENSE) for details.