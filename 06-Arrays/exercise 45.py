import matplotlib.pyplot as plt
import numpy as np

# Create an array of x values from 0 to 360 degrees converted to radians
x_degrees = np.arange(0, 361, 1)
x_radians = np.radians(x_degrees)

# Calculate y values for sin(x)
y = np.sin(x_radians)

# Plotting
plt.plot(x_degrees, y)
plt.title("Graph of y = sin(x) for x in range 0-360 degrees")
plt.xlabel("x (degrees)")
plt.ylabel("y = sin(x)")
plt.grid(True)
plt.show()
