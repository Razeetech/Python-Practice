import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#create a meshgrid of x and y values
x= np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
#define a functuon to calculate the z value(height) based on x and y
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))
#calculate the z value for the meshgrid
z = f(x, y)
#create a tree-dimentional countor plot

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")
contour = ax.contour3D(x, y, z, 50, cmaps="viridis")

#add labels and color bar

ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")
fig.colorbar(contour, ax=ax, label="z values")

#show the plot
plt.show()