from sympy import pprint, parse_expr, symbols, Float
from tabulate import tabulate


def print_table(dict):
    """
    Prints the dictionary as a table
    Assumes the following structure:
    {
      "n": {
        "x": value, "y": value
      },
      "n+1": {
        "x_1": value, "y_1": value
      }
      ...etc
    }
    """
    rows = [["n", "x_n", "y_n"]]
    for k, v in dict.items():
        rows.append([k, v["x"], v["y"]])

    print(tabulate(rows, headers="firstrow"))


def eulers_method(function, initial_x, initial_y, h, target_x):
    """
    Eurle's method for numerical solutions to First-Order DE

    function: should be of the form y' = f(x, y).
    Only include the right side of the euqation.
    Example: y' = y - x. The function argument should be y - x
    """
    values = {"x": Float(initial_x), "y": initial_y}
    approximations = {}
    exact_h = Float(h)

    n = 1
    while values["x"] < Float(target_x):
        approximations[n] = {
            "y": values["y"] + (exact_h * parse_expr(function, values)),
            "x": values["x"] + exact_h
        }

        values = {"x": values["x"] + exact_h, "y": approximations[n]["y"]}
        n += 1

    print_table(approximations)


if __name__ == "__main__":
    eulers_method("y - x", 0, .5, .1, 1)
