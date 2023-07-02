import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.axis([0,10,0,10])

castice = np.array([[1], [1]])  # x, y coordinates, x, y velocities

point = ax.plot(castice[0], castice[1], marker="o") # Access the first element of the list

def update(i):
    castice[0] = castice[0] + (0.1) * castice[2]
    castice[1] = castice[1] + (0.1) * castice[3]
    point.set_data([castice[0][0]], [castice[1][0]])  # Update the data of the line
    return point,

ani = FuncAnimation(fig, update, frames=range(100), interval=20)

plt.show()
