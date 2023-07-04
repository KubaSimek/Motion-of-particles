import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class Particle:
       def __init__(self, x, y, vx, vy, r):
             self.pos_x = x 
             self.pos_y = y
             self.vel_x = vx
             self.vel_y = vy
             self.radius = r
             
fig, ax = plt.subplots()
ax.axis([0, 10, 0, 10])


# Initial position and velocities
p1 = Particle(1,2,3,7,30)
point, = ax.plot(int(p1.pos_x), int(p1.pos_y), "o", mfc = "none", markersize = p1.radius)

prev_frame_time = 0

def update(frame):
    global p1, prev_frame_time
    current_time = frame * 0.001 
    dt = current_time - prev_frame_time
    prev_frame_time = current_time

    p1.pos_x += dt * p1.vel_x
    if 0 > p1.pos_x or 10 < p1.pos_x:
            p1.vel_x = -p1.vel_x
    p1.pos_y += dt * p1.vel_y
    if 0 > p1.pos_y or 10 < p1.pos_y:
            p1.vel_y = -p1.vel_y
    x = p1.pos_x
    y = p1.pos_y
    point.set_data(x, y)
    return point,

ani = FuncAnimation(fig, update, interval=100, frames=np.arange(0, 1000))
plt.show()
