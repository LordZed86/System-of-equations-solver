import sys
import numpy as np
from fractions import Fraction
from parser import parse_all
from solver import build_matrix, solve
from classifier import classify

# ANSI color codes
BLUE = "\033[34m"
GREEN = "\033[32m"
RED = "\033[31m"
GRAY = "\033[90m"
RESET = "\033[0m"


def format_value(val, use_fractions):
    """Format a float as either a decimal or a simplified fraction."""
    if use_fractions:
        frac = Fraction(val).limit_denominator(1000)
        if frac.denominator == 1:
            return str(frac.numerator)
        return f"{frac.numerator}/{frac.denominator}"
    return f"{val:>10.4f}"


def run(filepath=None, verbose=False, fraction=False):
    """
    Top-level runner. Parses file, solves each system, prints results.

    Args:
        filepath (str): path to input file
        verbose (bool): if True, prints augmented matrix before solving
        fraction (bool): if True, prints solutions as fractions
    """
    if filepath is None:
        args = sys.argv[1:]
        verbose = "-v" in args
        fraction = "-f" in args
        args = [a for a in args if a != "-v" and a != "-f"]

        if len(args) != 1:
            print("Usage: linear-solver [-v] [-f] <input_file>")
            sys.exit(1)
        filepath = args[0]

    try:
        systems = parse_all(filepath)
    except FileNotFoundError:
        print(f"{RED}Error: file '{filepath}' not found.{RESET}")
        sys.exit(1)

    print(f"{GRAY}{'=' * 40}{RESET}")
    for i, system in enumerate(systems):
        print(f"{BLUE}System {i + 1}:{RESET}")

        A, b, var_order = build_matrix(system)

        if verbose:
            print(f"\n{GRAY}  Augmented matrix [A|b]:{RESET}")
            print(f"{GRAY}  Variables: {var_order}{RESET}")
            augmented = np.column_stack((A, b))
            for row in augmented:
                formatted = "  [ " + "  ".join(f"{v:>8.4f}" for v in row[:-1]) + "  |  " + f"{row[-1]:>8.4f}" + " ]"
                print(f"{GRAY}{formatted}{RESET}")
            print()

        result = classify(A, b)

        if result == 'none':
            print(f"  {RED}No solution.{RESET}")
        elif result == 'infinite':
            print(f"  {RED}Infinite solutions.{RESET}")
        else:
            solution = solve(A, b)
            print(f"  {GREEN}One solution:{RESET}")
            max_var_len = max(len(v) for v in var_order)
            for var, val in zip(var_order, solution):
                val = 0.0 if abs(val) < 1e-10 else val
                formatted_val = format_value(val, fraction)
                print(f"    {GREEN}{var:<{max_var_len}} = {formatted_val}{RESET}")

        print(f"{GRAY}{'-' * 40}{RESET}")


if __name__ == "__main__":
    run()