import numpy as np


def build_matrix(system):
    """
    Build an augmented matrix [A|b] from a parsed system.

    Args:
        system (list[tuple]): list of (coefficients dict, constant) tuples
    Returns:
        tuple: (np.ndarray, np.ndarray, list[str]) -> (A, b, variable_order)
    """
    # collect all unique variables across all equations
    var_order = []
    for coeffs, _ in system:
        for var in coeffs:
            if var not in var_order:
                var_order.append(var)

    num_equations = len(system)
    num_vars = len(var_order)

    A = np.zeros((num_equations, num_vars))
    b = np.zeros(num_equations)

    for i, (coeffs, constant) in enumerate(system):
        b[i] = constant
        for var, coeff in coeffs.items():
            j = var_order.index(var)
            A[i][j] = coeff

    return A, b, var_order


def solve(A, b):
    """
    Attempt to solve the system Ax = b using numpy.
    Uses lstsq for overdetermined systems.

    Args:
        A (np.ndarray): coefficient matrix
        b (np.ndarray): constants vector
    Returns:
        np.ndarray: solution vector, or None if singular
    """
    try:
        num_equations, num_vars = A.shape
        if num_equations != num_vars:
            solution, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
            return solution
        return np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return None