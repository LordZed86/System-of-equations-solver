import numpy as np


def classify(A, b):
    """
    Determine if the system has one, none, or infinite solutions
    by comparing rank of A vs rank of augmented [A|b].

    Args:
        A (np.ndarray): coefficient matrix
        b (np.ndarray): constants vector
    Returns:
        str: 'one', 'none', or 'infinite'
    """
    pass