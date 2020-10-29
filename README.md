# numericalSolutions

This repo is my implementation of the Euler and Runga-Kutta methods for numerical solution to first-order differential equations. In [output.txt](https://github.com/camachom/numericalSolutions/blob/master/numericalMethods/output.txt) I have provided my results for problems 11-15 on page 101 of the book "Differential Equations and Linear Algebra" by Goode.

I solved [problem 11](https://github.com/camachom/numericalSolutions/blob/master/particularSolutions/ch_1_10_problem_11.pdf) and [problem 12](https://github.com/camachom/numericalSolutions/blob/master/particularSolutions/ch_1_10_problem_11.pdf) in `Latex` but I provided the PDFs for reference. This allowed me to graph and compare the actual solution against the numerical methods. 

## Summary of Results and Graphs

### Problem 11:
![Computation](images/computation_11.png?raw=true)
![Graph](images/problem_11_graph.png?raw=true)

### Problem 12:
![Computation](images/computation_12.png?raw=true)
![Graph](images/problem_12_graph.png?raw=true)

## Description

I wanted to avoid hard coding individual solutions, so I came up with a more general approach. Using `parse_expr`, `sympy` is able to take a string and convert it into an expression. For example:

```python
>>> from sympy import parse_expr
>>> str_expr = "x**2"
>>> parse_expr(str_expr, {"x": 8})
64
```

The rest is trivial. I just substitute for `x` and `y`, define the needed variables and evaluate the formula:

```python
  exact_h = Float(h)

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

  .... values["y"] + (1 / 6)*(k_1 + (2 * k_2) + (2 * k_3) + k_4)

```

The graphs were made using `matplotlib`.

## Bugs

I struggled with rounding errors. This was my first time using `sympy` and it does not play well with the `decimal` module out of the box. You will notice that some solutions are more accurate than others.

## How to use

This program is written in Python3 using the `sympy` and `tabulate` libraries. Once you have all dependencies installed, run:

```python
python3 ./solutions.py
```

