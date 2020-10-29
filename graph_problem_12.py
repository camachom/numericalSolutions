import matplotlib.pyplot as plt
import numpy as np
from math import e

import matplotlib.pyplot as plt
# problem 11

fig, ax = plt.subplots()  # Create a figure and an axes.
# Plot some data on the axes.
ax.plot([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5],
        [1.15, 1.33, 1.546, 1.8052, 2.11624, 2.48949,
            2.93739, 3.47486, 4.11984, 4.8938], "go",
        label="Euler's Method")

ax.plot(
    [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5],
    [1.16605, 1.36886, 1.61658, 1.91914, 2.28869,
        2.74005, 3.29135, 3.96471, 4.78714, 5.79167], "ro",
    label="Runge-Kutta's Method")

ax.plot(
    [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5],
    [1.166052069, 1.368868523, 1.6165891, 1.919155696, 2.288711371, 2.740087692,
        3.291399975, 3.964774318, 4.787235598, 5.791792074],
    label="Actual Solution")

ax.set_xlabel('x axis')  # Add an x-label to the axes.
ax.set_ylabel('y axis')  # Add a y-label to the axes.
ax.set_title('1.10 Problem 11')  # Add a title to the axes.
ax.legend()  # Add a legend.

plt.show()
