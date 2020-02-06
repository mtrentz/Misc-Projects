import numpy as np
from matplotlib import pyplot as plt

# Creates normalized slope field from a diff. equation


# Diff Equation to be plotted
def dif(y):
    dydt = 5 * y**2
    return dydt


# Axis span and number of lines in the slope field
w = np.linspace(-5, 5, 25)
v = np.linspace(-5, 5, 25)

# Just graph-style
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.set_facecolor('#071e3d')
fig.set_facecolor('#071e3d')
ax.tick_params(labelcolor='w', color='w')
for spine in ax.spines:  # Sets graph outline to color
    ax.spines[spine].set_color('w')

# Normalizing each slope vector
for x in v:
    for y in w:
        slope = dif(y)
        mag = 0.3   # Magnitude of vector
        # Expression to normalize in dependence of mag and slope
        coefs = [4, -8*x, (4 * x**2 - mag**2 / (1 + slope**2))]
        rts = np.roots(coefs)
        if (rts[0].real-x)**2 <= (rts[1].real-x)**2:
            x2 = rts[0].real
        else:
            x2 = rts[1].real
        x1 = 2 * x - x2
        y1 = (2 * y - slope * (x1 - x2)) / 2
        y2 = 2*y - y1
        ax.plot([x2, x1], [y1, y2], solid_capstyle='projecting', solid_joinstyle='bevel')

plt.show()






