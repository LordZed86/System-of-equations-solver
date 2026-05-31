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
    num_equations, num_vars = A.shape
    augmented = np.column_stack((A, b))
    rank_A = np.linalg.matrix_rank(A)
    rank_aug = np.linalg.matrix_rank(augmented)

    # overdetermined system — more equations than unknowns
    if num_equations > num_vars:
        if rank_A == rank_aug == num_vars:
            return 'one'
        return 'none'
    # rank comparison handles non-invertible matrices without calling numpy.linalg.solve
    if rank_A != rank_aug:
        return 'none'
    elif rank_A == rank_aug == num_vars:
        return 'one'
    else:
        return 'infinite'