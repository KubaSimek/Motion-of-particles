from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import bounce_functions as bf
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Colour of the particles
colour_darkblue = "#214478"

class Particle:
    def __init__(self, x, y, vx, vy, r, m):
        self.pos_x = x 
        self.pos_y = y
        self.vel_x = vx
        self.vel_y = vy
        self.radius = r
        self.pos_coord = np.array((x,y))
        self.vel_coord = np.array((vx,vy))
        self.point = None
        self.mass = m

    def plt_par(self,ax):
        self.point, = ax.plot(self.pos_x, self.pos_y, "bo", mfc = "none", markersize = self.radius*60)
    
    def __repr__(self):
        return("(x = " + str(self.pos_x) + ", y = " + str(self.pos_y) + ", vx = " + str(self.vel_x) + ", vy = " + str(self.vel_y) + ", r = " + str(self.radius) + ", m = " + str(self.mass) + ")")

fig, ax= plt.subplots()
animation_canvas = False
prev_frame_time = 0
class Particles:
    def __init__(self):
        self.par = []
        
    def add_par(self,par):
        self.par.append(par)
      
    def destroy_particles(self):
        self.par = []

    def print_par(self):
        return(print(self.par))
    
    def innit_anim_on_canvas(self,x):
        global fig, animation_canvas
        animation_canvas = FigureCanvasTkAgg(figure = fig, master= x)
        animation_canvas.get_tk_widget().place(x = 500, y = 62, anchor="nw", height = 440, width = 440)
    
    def animation(self,x, save = False):
        global fig, ax
        for s in ['top','bottom','left','right']:
            ax.spines[s].set_linewidth(2)
        ax.set_aspect('equal', 'box')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        fig.tight_layout(pad=0)

        for p in self.par:
            p.plt_par(ax)
        
        def position_update(dt):
            for p in self.par:
                p.pos_x += dt * p.vel_x
                p.pos_y += dt * p.vel_y 

        def update(frame):
            global prev_frame_time
            current_time = frame * 0.001 
            dt = current_time - prev_frame_time
            prev_frame_time = current_time

            for p in particles.par:
                p.pos_coord = np.array((p.pos_x,p.pos_y))
                p.vel_coord = np.array((p.vel_x,p.vel_y))

            bf.wall_bounce(self)
            bf.particles_bounce()
            
            position_update(dt)
            
            for p in self.par:
                p.point.set_data([p.pos_x],[p.pos_y])
            
            return

        if save == True:
            pass
        else:    
            ani = FuncAnimation(fig, update, interval=1, cache_frame_data=False)
            x.mainloop()


particles = Particles()
def add_par(x,y,vx,vy,r,m):
    particles.add_par(Particle(x,y,vx,vy,r,m))
