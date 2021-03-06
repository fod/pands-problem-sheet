# plottask.py
# Produce plot of linear, quadratic, and cubic functions: 
# f(x) = x, f(x) = x^2 and f(x) = x^3
# Author: Fiachra O' Donoghue

# Import the matplotlib.pyplot library and alias to plt
import matplotlib.pyplot as plt

# Import numpy array manipulation library and alias to np
import numpy as np

# Create a list containing 100 numbers evenly spaced from 0 to 4
x = np.linspace(0,4,100)

# Plot the three functions
# https://stackoverflow.com/questions/21226868/superscript-in-python-plots
plt.plot(x, x, label = "f(x) = x")
plt.plot(x, x**2, label = "f(x) = $x^2$")
plt.plot(x, x**3, label = "f(x) = $x^3$")

# Add legend using the labels specified in the plot() arguments
plt.legend()

# Display the plot
plt.show()
