# System of Linear Equations Solver

## Introduction

This program solves systems of linear equations provided as a list of strings. Each string  
represents one equation with variables on the left side and a constant on the right 
(e.g., `"2x + 3y - z = 5"`). The program will parse each equation, construct a matrix 
representation of the system, and apply linear algebra techniques to determine whether the 
system has one solution, no solution, or infinitely many — outputting variable values where 
applicable.

---

## Data Flow

1. File input — Read the text file and load its full contents
2. Split systems — Split contents on `;` to get individual systems as strings
3. Split equations — For each system, split on `,` to get individual equation strings
4. Parse equations — Tokenize each string, extract coefficients and variable names, handle 
   negatives and missing coefficients (e.g., bare `x = 1`, `-x = -1`)
5. Build matrix — Construct an augmented matrix `[A|b]` where `A` holds coefficients and `b` holds 
   constants
6. Solve — Apply Gaussian elimination or use `numpy.linalg` to solve the system
7. Classify — Determine if the system has `one solution`, `no solution`, or `infinite solutions`
8. Output — For each system, print solution count and variable values (or appropriate message)

---

## Priority Task List

1. File parser — Read file, split on `;` and `,` to produce lists of equation strings per system
2. Equation parser — Tokenize each equation string, extract coefficients and variables; this is 
   the most critical and complex step
3. Matrix builder — Map parsed coefficients to the correct columns, treating missing variables as 
   `0-coefficient` columns
4. Solver — Use `numpy.linalg.solve` to start; add fallback logic for edge cases
5. Solution classifier — Detect `no solution` vs. `infinite solutions` using rank comparison of 
   `A` and `[A|b]`
6. Output formatter — Display results clearly for each system in the file
7. Error handling — Validate input and catch solver failures
8. Testing — Write unit tests first → Write white box tests at each stage → Write systems tests 
   to validate the program at the end.

---

## Estimated Schedule

| Date   | Milestone                                       |
|--------|-------------------------------------------------|
| May 23 | File parser + equation parser complete          |
| May 28 | Matrix builder + solver working end-to-end      |
| June 2 | Solution classifier + output formatter complete |
| June 5 | Error handling + edge cases covered             |
| June 7 | Testing complete, all cases passing             |
| June 9 | Final review + submission                       |

---

## Error Handling

- Malformed input — equation strings that don't match the expected format (missing =, invalid 
  characters, empty strings); catch during parsing and raise a descriptive error
- Inconsistent variables — e.g., one equation uses x and y, another uses x and z; handle by 
  treating missing variables as `0-coefficient` columns
- No solution / infinite solutions — not true errors but **must be caught before calling numpy** 
  if using `numpy.linalg.solve`, which will throw a `LinAlgError` on a singular matrix
- Non-numeric constants — e.g., `"2x + 3y = abc"`; catch during parsing
- Empty system — a semicolon with nothing between it and the next; skip or raise a descriptive error
- File not found — wrap file open in a `try/except` and exit with a clear message

---

## Performance Considerations

- Parsing — iterating over every token in every equation is `O(n·m)` where `n` is equations and 
  `m` is  terms; fine at small scale but not optimal at a larger scale
- Matrix operations — Gaussian elimination is estimated at `O(n³)`; numpy uses LU decomposition 
  with optimized BLAS routines to utilize multithreading which can make this faster, but large 
  systems will still be slow. So Asymptotics become system dependant but still not great.
- Variable tracking — build the variable-to-column mapping in one pass using a dict to avoid 
  redundant lookups
- Multiple systems — each system is solved independently so complexity will scale linearly with 
  the number of systems in the file

---

## Testing and Quality Assurance

- Standard case — a well-formed system with one unique solution; verify correct variable values
- No solution — contradictory equations (e.g., `x + y = 1` and `x + y = 2`); verify correct message
- Infinite solutions — underdetermined system (fewer equations than unknowns); verify correct  
  message
- Single equation / single variable — minimal valid input
- Missing variables — one equation uses `z`, another doesn't; verify `z` gets a `0-coefficient` column
- Negative coefficients — e.g., `-x + 4y = 2`; verify sign is parsed correctly
- Bare variables — `x` with no coefficient treated as `1x`
- Multiple systems in one file — verify each system is solved independently and all results are 
  reported
- Mixed results — a file where one system has a solution and another doesn't; verify both outputs 
  are correct
- Malformed equation mid-file — verify the error is reported without crashing the rest of the run
- Empty system — a stray `;` in the file; verify graceful handling

---

## Dependencies / Tech Stack

- `Python 3.x` — core language
- `numpy` — matrix construction and solving (default choice; revisit if performance becomes a concern)
- `File I/O` — standard library only (`open`, `readlines`)
- Testing framework — `unittest` or `pytest` (may or may not be necessary for this project)

---

## Assumptions

- Input is provided as a text file following the specified format
- Equations within a system are comma-separated; systems are semicolon-separated
- Variables are single lowercase letters only
- Coefficients and operators are space-separated
- The number of equations and variables is small enough for dense matrix methods (revisit if 
  scale requirements change)
- No UI is required at this time (confirm with instructor)