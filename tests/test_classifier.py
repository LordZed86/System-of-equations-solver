import pytest
import numpy as np
from classifier import classify


def test_one_solution():
    """standard solvable system"""
    A = np.array([[2.0, 3.0], [-1.0, 4.0]])
    b = np.array([5.0, 2.0])
    assert classify(A, b) == 'one'

def test_no_solution():
    """contradictory system"""
    A = np.array([[1.0, 1.0], [1.0, 1.0]])
    b = np.array([1.0, 2.0])
    assert classify(A, b) == 'none'

def test_infinite_solutions():
    """underdetermined system"""
    A = np.array([[1.0, 1.0], [2.0, 2.0]])
    b = np.array([3.0, 6.0])
    assert classify(A, b) == 'infinite'

def test_three_variables_one_solution():
    """3x3 system with unique solution"""
    A = np.array([[2.0, 1.0, -1.0],
                  [-3.0, -1.0, 2.0],
                  [-2.0, 1.0, 2.0]])
    b = np.array([8.0, -11.0, -3.0])
    assert classify(A, b) == 'one'

def test_overdetermined_one_solution():
    """overdetermined system with consistent equations should return one"""
    A = np.array([[1.0, 1.0],
                  [2.0, 1.0],
                  [1.0, -1.0]])
    b = np.array([3.0, 5.0, 1.0])
    assert classify(A, b) == 'one'

def test_overdetermined_no_solution():
    """overdetermined system with contradictory equations should return none"""
    A = np.array([[1.0, 1.0],
                  [1.0, 1.0],
                  [1.0, 1.0]])
    b = np.array([3.0, 4.0, 5.0])
    assert classify(A, b) == 'none'