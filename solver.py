import numpy as np


def build_matrix(system):
    """
    Build an augmented matrix [A|b] from a parsed system.

    Args:
        system (list[tuple]): list of (coefficients dict, constant) tuples
    Returns:
        tuple: (np.ndarray, np.ndarray, list[str]) -> (A, b, variable_order)
    """
    pass


def solve(A, b):
    """
    Attempt to solve the system Ax = b using numpy.

    Args:
        A (np.ndarray): coefficient matrix
        b (np.ndarray): constants vector
    Returns:
        np.ndarray: solution vector, or None if singular
    """
    pass