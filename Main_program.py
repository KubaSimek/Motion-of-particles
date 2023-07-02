import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.axis([0, 10, 0, 10])

# Initial position and velocities
x, y = 1, 1
vx, vy = 200, 170

point, = ax.plot(x, y, marker="o")  # Note the comma after "point" to unpack the tuple

def update(i):
    global x, y, vx, vy # To access and modify the variables outside the function scope
    x += 0.001 * vx
    if 0 > x or 10 < x:
            vx = -vx
    y += 0.001 * vy
    if 0 > y or 10 < y:
            vy = -vy

    point.set_data(x, y)  # Set data for the point
    return point,

ani = FuncAnimation(fig, update, interval=1)

plt.show()