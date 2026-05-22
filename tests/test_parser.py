import pytest
from parser import load_file, split_equations, parse_equation, parse_all


# --- load_file tests ---

def test_load_file_returns_list():
    """load_file should return a list"""
    result = load_file("tests/fixtures/simple.txt")
    assert isinstance(result, list)

def test_load_file_splits_on_semicolon():
    """multiple systems should produce multiple entries"""
    result = load_file("tests/fixtures/two_systems.txt")
    assert len(result) == 2

def test_load_file_not_found():
    """missing file should raise FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        load_file("tests/fixtures/nonexistent.txt")


# --- split_equations tests ---

def test_split_equations_basic():
    """should split on commas"""
    result = split_equations("2x + 3y = 5, -x + 4y = 2")
    assert len(result) == 2

def test_split_equations_single():
    """single equation should return list of one"""
    result = split_equations("2x + 3y = 5")
    assert len(result) == 1

def test_split_equations_strips_whitespace():
    """each equation string should be stripped"""
    result = split_equations("2x + 3y = 5 , -x + 4y = 2")
    assert result[0] == "2x + 3y = 5"
    assert result[1] == "-x + 4y = 2"


# --- parse_equation tests ---

def test_parse_equation_basic():
    """standard equation parses correctly"""
    coeffs, const = parse_equation("2x + 3y = 5")
    assert coeffs == {"x": 2.0, "y": 3.0}
    assert const == 5.0

def test_parse_equation_negative_coefficient():
    """-x should parse as -1.0"""
    coeffs, const = parse_equation("-x + 4y = 2")
    assert coeffs == {"x": -1.0, "y": 4.0}
    assert const == 2.0

def test_parse_equation_bare_variable():
    """bare variable with no coefficient should be 1.0"""
    coeffs, const = parse_equation("x + y = 3")
    assert coeffs["x"] == 1.0
    assert coeffs["y"] == 1.0

def test_parse_equation_subtraction():
    """subtraction should produce negative coefficient"""
    coeffs, const = parse_equation("a - b + c - x = 2")
    assert coeffs["b"] == -1.0
    assert coeffs["x"] == -1.0

def test_parse_equation_negative_constant():
    """negative constant on right side"""
    coeffs, const = parse_equation("2x + 3y = -5")
    assert const == -5.0

def test_parse_equation_invalid_no_equals():
    """missing equals sign should raise ValueError"""
    with pytest.raises(ValueError):
        parse_equation("2x + 3y 5")

def test_parse_equation_invalid_constant():
    """non-numeric constant should raise ValueError"""
    with pytest.raises(ValueError):
        parse_equation("2x + 3y = abc")


# --- parse_all tests ---

def test_parse_all_structure():
    """should return a list of systems, each a list of tuples"""
    result = parse_all("tests/fixtures/simple.txt")
    assert isinstance(result, list)
    assert isinstance(result[0], list)
    assert isinstance(result[0][0], tuple)

def test_parse_all_two_systems():
    """file with two systems should return two systems"""
    result = parse_all("tests/fixtures/two_systems.txt")
    assert len(result) == 2