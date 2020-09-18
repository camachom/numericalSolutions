from sympy import pprint, parse_expr, symbols, Float, Rational, sympify, lambdify
from tabulate import tabulate
from decimal import *


def print_table(euler, runge):
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
    rows = [["n", "x_n", "Euler's Method",
             "Runge-Kutta's Method", "|Runge - Euler|"]]
    for k, v in euler.items():
        rows.append([k, v["x"], v["y"], runge[k]["y"],
                     abs(runge[k]["y"] - v["y"])])

    print(tabulate(rows, headers="firstrow"))


def eulers_method(function, initial_x, initial_y, h, target_x):
    """
    Eurle's method for numerical solutions to First-Order DE

    function: should be of the form y' = f(x, y).
    Only include the right side of the euqation.
    Example: y' = y - x. The function argument should be y - x
    """
    values = {"x": Decimal(initial_x), "y": Decimal(initial_y)}
    approximations = {}
    exact_h = Decimal(h)

    n = 1
    while values["x"] < Decimal(target_x):
        approximations[n] = {
            "y": values["y"] + (exact_h * parse_expr(function, values)),
            "x": values["x"] + exact_h
        }

        values = {"x": values["x"] + exact_h, "y": approximations[n]["y"]}
        n += 1

    return approximations


def runge_kutta_method(function, initial_x, initial_y, h, target_x):
    values = {"x": Decimal(initial_x), "y": Decimal(initial_y)}
    approximations = {}
    exact_h = Decimal(h)

    n = 1
    while values["x"] < Decimal(target_x):
        k_1 = exact_h * parse_expr(function, values)
        k_2 = parse_expr(function, evaluate=False)

        k_3 = exact_h * parse_expr(function, {
            "x": values["x"] + (Float(Rational(1 / 2), 8) * exact_h),
            "y": values["y"] + (Float(Rational(1 / 2), 8) * k_2)
        })
        k_4 = exact_h * parse_expr(function, {
            "x": values["x"] + exact_h,
            "y": values["y"] + k_3
        })

        if n == 1:
            testing = lambdify(
                ["x", "y"], parse_expr(function), "numpy")
            print(exact_h * testing(Decimal(values["x"]) + (Decimal(0.5) *
                                                            Decimal(exact_h)), Decimal(values["y"]) + Decimal(0.5) * k_1))
            print("******************")

        approximations[n] = {
            "y": (
                values["y"] +
                Decimal((1 / 6)*(k_1 + (2 * k_2) + (2 * k_3) + k_4))
            )
        }

        values = {"x": values["x"] + exact_h, "y": approximations[n]["y"]}
        n += 1

    return approximations


"""
arguments for problems 1 - 5, pg 101 in order.
function, initial_x, initial_y, h, target_x
"""
PROBLEMS = [
    ["4*y - 1", 0, 1, 0.05, 0.5],
    ["- (2 * x * y) / (1 + x**2)", 0, 1, 0.1, 1],
    ["x - y**2", 0, 2, 0.05, 0.5],
    ["-1 * (x*x) * y", 0, 1, 0.2, 1],
    ["2 * x * y**2", 0, 0.5, 0.1, 1]


]

if __name__ == "__main__":
    problem = ["-(x**2) * y", 0, 1, 0.2, 1]
    euler = eulers_method(*problem)
    runge = runge_kutta_method(*problem)
    print_table(euler, runge)
    # for index, problem in enumerate(PROBLEMS):
    #     print("******************")
    #     print("Problem", index + 11)
    #     pprint(parse_expr(problem[0]))
    #     print("******************")
    #     euler = eulers_method(*problem)
    #     runge = runge_kutta_method(*problem)
    #     print_table(euler, runge)
