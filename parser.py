"""
Split on = to separate left and right sides
Split the left side on spaces to get tokens
Walk through tokens tracking the current sign
For each term, separate the numeric part from the letter part
"""

def load_file(filepath):
    """
    Read the input file and return a list of raw system strings.
    Splits the file contents on ';' to separate systems.

    Args:
        filepath (str): path to the input file
    Returns:
        list[str]: one string per system, unsplit
    """
    with open(filepath, 'r') as file:
        # return the entire contents of the file
        content = file.read()

        # divide strings into a list based on the semicolon
        # remove leading/trailing whitespace and newlines
        systems = [system.strip() for system in content.split(';') if system.strip()]

        return systems


def split_equations(system_str):
    """
    Take a single system string and split on ',' to get individual equations.

    Args:
        system_str (str): a single system e.g. "2x + 3y = 5, -x + 4y = 2"
    Returns:
        list[str]: individual equation strings
    """
    return [eq.strip() for eq in system_str.split(',') if eq.strip()]


def parse_equation(equation_str):
    """
    Parse a single equation string into a dict of {variable: coefficient}
    and a constant value.

    Args:
        equation_str (str): e.g. "2x + 3y - z = 5"
    Returns:
        tuple: (dict[str, float], float) -> (coefficients, constant)
    """
    if '=' not in equation_str:
        raise ValueError("Equation must contain exactly one '=' sign.")

    lhs, rhs = equation_str.split('=')
    lhs = lhs.strip()
    rhs = rhs.strip()

    # parse the constant
    try:
        constant = float(rhs)
    except ValueError:
        raise ValueError(f"Right-hand side must be a number, got '{rhs}'")

    coefficients = {}
    tokens = lhs.split()
    sign = 1

    for token in tokens:
        if token == '+':
            sign = 1
        elif token == '-':
            sign = -1
        else:
            # separate numeric and alpha parts
            var = ""
            coeff_str = ""
            for char in token:
                if char.isalpha():
                    var += char
                else:
                    coeff_str += char

            # handle attached leading minus e.g. "-x" or "-2x"
            if coeff_str == '-':
                coeff = -1.0
            elif coeff_str == '':
                coeff = 1.0
            else:
                coeff = float(coeff_str)

            coeff *= sign
            sign = 1  # reset sign after using it

            if var:
                coefficients[var] = coefficients.get(var, 0.0) + coeff

    return coefficients, constant


def parse_all(filepath):
    """
    Top-level function. Loads file, splits systems and equations,
    parses each equation, and returns structured data for the solver.

    Args:
        filepath (str): path to the input file
    Returns:
        list[list[tuple]]: a list of systems, each system is a list of
                           (coefficients dict, constant) tuples
    """
    systems = load_file(filepath)
    all_systems = []
    for system in systems:
        equations = split_equations(system)
        current_system = []
        for eq in equations:
            current_system.append(parse_equation(eq))
        all_systems.append(current_system)
    return all_systems

