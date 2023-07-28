import matplotlib.pyplot as plt
import numpy as np
import bounce_functions as bf
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

class Particle:
       def __init__(self, x, y, vx, vy, r, d = 1, m = None):
             self.name = self
             self.pos_x = x 
             self.pos_y = y
             self.vel_x = vx
             self.vel_y = vy
             self.radius = r
             self.pos_coord = np.array((x,y))
             self.vel_coord = np.array((vx,vy))
             self.density = d
             if m == None:
                   self.mass = d * (np.pi * r**2)
             else:
                   self.mass = m
       
       def plt_par(self,ax):
             point = ax.plot(self.pos_x, self.pos_y, "o", mfc = "none", markersize = self.radius)
             return point

class Particles:
       def __init__(self):
             self.par = []
        
       def add_par(self,par):
             self.par.append(par)
       
       def print_par(self):
             return(print(self.par))


particles = Particles()
p1 = Particle(1,2,100,90,10)
p2 = Particle(7,8,-80,-110,15)
p3 = Particle(8,6,30,99,50)

particles.add_par(p1)
particles.add_par(p2)
particles.add_par(p3)
             
fig, ax = plt.subplots()
for s in ['top','bottom','left','right']:
        ax.spines[s].set_linewidth(2)
        ax.set_aspect('equal', 'box')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
particles_plots = []


prev_frame_time = 0

bf.pairs_of_particles(particles.par)



def position_update(dt):
      for p in particles.par():
            p.pos_x += dt * p.vel_x
            p.pos_y += dt * p.vel_y 
            p.plt_par(ax)

def update(frame):
    global p1, p2, prev_frame_time
    current_time = frame * 0.001 
    dt = current_time - prev_frame_time
    prev_frame_time = current_time

    bf.wall_bounce(particles)
    bf.particles_bounce()

    for p in particles.par():
            p.pos_x += dt * p.vel_x
            p.pos_y += dt * p.vel_y 
            p.plt_par(ax)
    
    return 

ani = FuncAnimation(fig, update, interval=1)
plt.show()

