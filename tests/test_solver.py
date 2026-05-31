import pytest
import numpy as np
from solver import build_matrix, solve


# --- build_matrix tests ---

def test_build_matrix_returns_tuple():
    """build_matrix should return a tuple of (A, b, variable_order)"""
    system = [
        ({"x": 2.0, "y": 3.0}, 5.0),
        ({"x": -1.0, "y": 4.0}, 2.0)
    ]
    result = build_matrix(system)
    assert isinstance(result, tuple)
    assert len(result) == 3

def test_build_matrix_shape():
    """A should be 2x2 and b should be length 2 for a 2 equation 2 variable system"""
    system = [
        ({"x": 2.0, "y": 3.0}, 5.0),
        ({"x": -1.0, "y": 4.0}, 2.0)
    ]
    A, b, var_order = build_matrix(system)
    assert A.shape == (2, 2)
    assert b.shape == (2,)

def test_build_matrix_missing_variable():
    """variable missing from one equation should get 0.0 coefficient"""
    system = [
        ({"x": 1.0, "y": 2.0}, 3.0),
        ({"x": 1.0}, 1.0)
    ]
    A, b, var_order = build_matrix(system)
    y_col = var_order.index("y")
    assert A[1][y_col] == 0.0

def test_build_matrix_constants():
    """b vector should match the constants from each equation"""
    system = [
        ({"x": 2.0, "y": 3.0}, 5.0),
        ({"x": -1.0, "y": 4.0}, 2.0)
    ]
    A, b, var_order = build_matrix(system)
    assert list(b) == [5.0, 2.0]

def test_build_matrix_variable_order():
    """var_order should contain all variables in the system"""
    system = [
        ({"x": 2.0, "y": 3.0}, 5.0),
        ({"x": -1.0, "y": 4.0}, 2.0)
    ]
    A, b, var_order = build_matrix(system)
    assert set(var_order) == {"x", "y"}


# --- solve tests ---

def test_solve_basic():
    """standard 2x2 system should return correct solution"""
    A = np.array([[2.0, 3.0], [-1.0, 4.0]])
    b = np.array([5.0, 2.0])
    result = solve(A, b)
    assert result is not None
    assert np.allclose(result, np.linalg.solve(A, b))

def test_solve_returns_ndarray():
    """solve should return a numpy array"""
    A = np.array([[1.0, 0.0], [0.0, 1.0]])
    b = np.array([3.0, 4.0])
    result = solve(A, b)
    assert isinstance(result, np.ndarray)

def test_solve_singular_matrix():
    """singular matrix should return None, not raise"""
    A = np.array([[1.0, 2.0], [2.0, 4.0]])
    b = np.array([3.0, 6.0])
    result = solve(A, b)
    assert result is None

def test_solve_identity():
    """identity matrix should return b as solution"""
    A = np.array([[1.0, 0.0], [0.0, 1.0]])
    b = np.array([7.0, 3.0])
    result = solve(A, b)
    assert np.allclose(result, [7.0, 3.0])

def test_solve_three_variables():
    """3x3 system should solve correctly"""
    A = np.array([[2.0, 1.0, -1.0],
                  [-3.0, -1.0, 2.0],
                  [-2.0, 1.0, 2.0]])
    b = np.array([8.0, -11.0, -3.0])
    result = solve(A, b)
    assert np.allclose(result, [2.0, 3.0, -1.0])