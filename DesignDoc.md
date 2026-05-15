# System of Linear Equations Solver

## Introduction

This program solves systems of linear equations provided as a list of strings. Each string  
represents one equation with variables on the left side and a constant on the right 
(e.g., `"2x + 3y - z = 5"`). The program will parse each equation, construct a matrix 
representation of the system, and apply linear algebra techniques to determine whether the system has one 
solution, no solution, or infinitely many — outputting variable values where applicable.

---

## Data Flow

1. Input — Receive a list of equation strings (e.g., `["2x + 3y = 5", "-x + 4y = 2"]`)
2. File input (optional) — If a file path is provided, read it line by line and build the equation 
   list automatically; otherwise accept a list of strings directly
3. Parse — Tokenize each string, extract coefficients and variable names, handle negatives and 
   missing coefficients (e.g., bare `x = 1`, `-x = -1`)
4. Build matrix — Construct an augmented matrix `[A|b]` where A holds coefficients and b holds 
   constants
5. Solve — Apply Gaussian elimination (or use `numpy.linalg`) to solve the system
6. Classify — Determine if the system has `one solution`, `no solution`, or `infinite solutions`
7. Output — Print solution count and variable values (or appropriate message)

---

## Priority Task List

1. String parser — This is the hardest and most critical piece; everything else depends on clean 
input
2. Matrix builder — Map parsed coefficients to the right columns, handling any variables that are 
   missing from some equations (coefficient = 0)
3. Solver — Use numpy.linalg.solve to start; add fallback logic for edge cases
4. Solution classifier — Detect no solution vs. infinite solutions using rank comparison of A and 
   [A|b]
5. Output formatter — Display results cleanly
6. Error handling — Validate input strings and catch solver failures
7. Testing — Write tests at each stage, not just at the end

---

## Error Handling

- **Malformed input** — equation strings that don't match the expected format (missing =, invalid 
characters, empty strings); catch during parsing and raise a descriptive error
- **Inconsistent variables** — e.g., one equation uses x and y, another uses x and z; handle by 
  treating missing variables as 0-coefficient columns
- **No solution / infinite solutions** — not true errors but need to be caught before calling numpy.
  linalg.solve, which will throw a LinAlgError on a singular matrix
- **Noninteger / non-numeric constants** — e.g., "2x + 3y = abc"; catch during parsing
- Empty input — an empty list or list of blank strings; return early with a clear message

---

## Performance Considerations

- **Parsing** — iterating over every token in every string is O(n·m) where n is equations and m is 
terms; fine at small scale but could slow on very large systems
- **Matrix operations** — Gaussian elimination is O(n³); numpy mitigates this with optimized BLAS 
  routines but large systems (hundreds of variables) will still be slow
- **Variable tracking** — building and looking up the variable-to-column mapping on every parse 
  step could be optimized with a dict built in one pass
- **Scalability** — for very large systems, scipy.sparse solvers would be more appropriate than 
  dense numpy arrays

---

## Testing and Quality Assurance

- Standard case — a well-formed system with one unique solution; verify correct variable values
- No solution — contradictory equations (e.g., x + y = 1 and x + y = 2); verify correct message
- Infinite solutions — underdetermined system (fewer equations than unknowns); verify correct 
  message
- Single equation / single variable — minimal valid input
- Missing variables — one equation uses z, another doesn't; verify z gets a 0-coefficient column
- Negative coefficients — e.g., -x + 4y = 2; verify sign is parsed correctly
- Bare variables — x with no coefficient should be treated as 1x
- Malformed strings — missing =, garbage input; verify descriptive errors are raised
- Empty input — empty list; verify graceful exit
- File import — test with a well-formed file, a file with blank lines, and a file with a 
  malformed equation somewhere in the middle

---

## Dependencies / Tech Stack

- Python 3.x — core language
- numpy — matrix construction and solving (default choice; revisit if performance becomes a concern)
- scipy — (optional; consider if large sparse systems are needed)
- File I/O — standard library only (open, readlines)
- Testing framework — unittest or pytest (TBD — confirm preference)

---

## Assumptions

- Equations are provided in the expected format; the parser will not attempt to fix heavily 
malformed input
- Variables are single lowercase letters only
- Coefficients and operators are space-separated
- The number of equations and variables is small enough for dense matrix methods (revisit if 
  scale requirements change)
- No UI is required at this time (confirm with instructor)
