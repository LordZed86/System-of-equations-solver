from parser import parse_all
from solver import build_matrix, solve
from classifier import classify


def run(filepath):
    """
    Top-level runner. Parses file, solves each system, prints results.

    Args:
        filepath (str): path to input file
    """
    pass


if __name__ == "__main__":
    import sys
    run(sys.argv[1])