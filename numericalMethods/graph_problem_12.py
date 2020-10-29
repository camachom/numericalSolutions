import matplotlib.pyplot as plt
import numpy as np
from math import e

import matplotlib.pyplot as plt
# problem 12

fig, ax = plt.subplots()  # Create a figure and an axes.
# Plot some data on the axes.
ax.plot([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
        [1, 1, 0.980198, 0.942498, 0.890617, 0.829196, 0.76286,
            0.695549, 0.630195, 0.568713, 0.512156], "go",
        label="Euler's Method")

ax.plot(
    [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
    [1, 0.990099, 0.961538, 0.917431, 0.862069, 0.8,
        0.735294, 0.671141, 0.609756, 0.552486, 0.5], "ro",
    label="Runge-Kutta's Method")

ax.plot(
    [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
    [1, 0.990099, 0.961538, 0.917431, 0.862069, 0.8,
        0.735294, 0.671141, 0.609756, 0.552486, 0.5],
    label="Actual Solution")

ax.set_xlabel('x axis')  # Add an x-label to the axes.
ax.set_ylabel('y axis')  # Add a y-label to the axes.
ax.set_title('1.10 Problem 12')  # Add a title to the axes.
ax.legend()  # Add a legend.

plt.show()
