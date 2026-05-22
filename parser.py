def load_file(filepath):
    """
    Read the input file and return a list of raw system strings.
    Splits the file contents on ';' to separate systems.

    Args:
        filepath (str): path to the input file
    Returns:
        list[str]: one string per system, unsplit
    """
    pass


def split_equations(system_str):
    """
    Take a single system string and split on ',' to get individual equations.

    Args:
        system_str (str): a single system e.g. "2x + 3y = 5, -x + 4y = 2"
    Returns:
        list[str]: individual equation strings
    """
    pass


def parse_equation(equation_str):
    """
    Parse a single equation string into a dict of {variable: coefficient}
    and a constant value.

    Args:
        equation_str (str): e.g. "2x + 3y - z = 5"
    Returns:
        tuple: (dict[str, float], float) -> (coefficients, constant)
    """
    pass


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
    pass