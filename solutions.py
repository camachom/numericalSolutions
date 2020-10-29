from sympy import pprint, parse_expr, Float
from tabulate import tabulate


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
             "Runge-Kutta's Method", "|Runge - Euler|", "Soltuion"]]
    for k, v in euler.items():
        rows.append([k, v["x"], v["y"], runge[k]["y"],
                     abs(runge[k]["y"] - v["y"]), runge[k]["solution"]])

    print(tabulate(rows, headers="firstrow"))


def eulers_method(function, initial_x, initial_y, h, target_x, solution):
    """
    Euler's method for numerical solutions to First-Order DE

    function: should be of the form y' = f(x, y).
    Only include the right side of the euqation.
    Example: y' = y - x. The function argument should be y - x
    """
    values = {"x": Float(initial_x), "y": Float(initial_y)}
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

        if n == 11:
            break

    return approximations


def runge_kutta_method(function, initial_x, initial_y, h, target_x, solution):
    """
    Runge-Kutta's method for numerical solutions to First-Order DE

    function: should be of the form y' = f(x, y).
    Only include the right side of the euqation.
    Example: y' = y - x. The function argument should be y - x
    """
    values = {"x": Float(initial_x), "y": Float(initial_y)}
    approximations = {}
    exact_h = Float(h)

    n = 1
    while values["x"] < Float(target_x):
        k_1 = exact_h * parse_expr(function, values)
        k_2 = exact_h * parse_expr(function, {
            "x": values["x"] + (0.5 * exact_h),
            "y": values["y"] + (0.5 * k_1)
        })
        k_3 = exact_h * parse_expr(function, {
            "x": values["x"] + (0.5 * exact_h),
            "y": values["y"] + (0.5 * k_2)
        })
        k_4 = exact_h * parse_expr(function, {
            "x": values["x"] + exact_h,
            "y": values["y"] + k_3
        })

        approximations[n] = {
            "x": values["x"],
            "y": (
                values["y"] +
                (1 / 6)*(k_1 + (2 * k_2) + (2 * k_3) + k_4)
            ),
            "solution": parse_expr(solution, {"x": values["x"] + exact_h})
        }

        values = {"x": values["x"] + exact_h, "y": approximations[n]["y"]}
        n += 1

        if n == 11:
            break

    return approximations


"""
arguments for problems 1 - 5, pg 101 in order.
function, initial_x, initial_y, h, target_x, solution
"""
PROBLEMS = [
    ["4*y - 1", 0, 1, 0.05, 0.5, "(1/4)*(3*e**(4*x) + 1)"],
    ["- (2 * x * y) / (1 + x**2)", 0, 1, 0.1, 1, "1 / (x**2 + 1)"],
    ["x - y**2", 0, 2, 0.05, 0.5, "0"],
    ["-1 * (x*x) * y", 0, 1, 0.2, 1, "e**(-x**3 / 3)"],
    ["2 * x * y**2", 0, 0.5, 0.1, 1, "-(1 / (x**2 - 2))"],
]

if __name__ == "__main__":
    for index, problem in enumerate(PROBLEMS):
        print("******************")
        print("Problem", index + 11)
        pprint(parse_expr(problem[0]))
        print("******************")
        runge = runge_kutta_method(*problem)
        euler = eulers_method(*problem)
        print_table(euler, runge)
