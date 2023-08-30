"""
SIMULATION OF 2D PARTICLES IN A BOX

This python program creates an animation (simulation)
displayed in the user interface in the gui.py file 
and using the functions in the bounce_functions file.

To learn more about this project, read the ABOUT file.
"""

from typing import Any
import matplotlib.pyplot as plt
import numpy as np
import bounce_functions as bf
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# A colour that is used on particles plots
colour_darkblue = "#214478"

class Particle:
    def __init__(self, x, y, vx, vy, r, m):
        """
        Initialization of a particle with its parametres
        """
        self.pos_x = x 
        self.pos_y = y
        self.vel_x = vx
        self.vel_y = vy
        self.radius = r
        self.mass = m
        #Position and velocity coordinants in array to easier manipulation during computing collisions
        self.pos_coord = np.array((x,y))
        self.vel_coord = np.array((vx,vy))
        self.point = None #This parameter is used for plotting the particle

    def plt_par(self,ax):
        """
        This method is used to plot the particle on the canvas
        """
        self.point, = ax.plot(self.pos_x, self.pos_y, "bo", mfc = "none", markersize = self.radius*60)
    
    def __repr__(self):
        """
        This method is used to print informations about the particle
        """
        return("(x = " + str(self.pos_x) + ", y = " + str(self.pos_y) + ", vx = " + str(self.vel_x) + 
               ", vy = " + str(self.vel_y) + ", r = " + str(self.radius) + ", m = " + str(self.mass) + ")")

# These variables are also used in other files, so it is easier to put them as global (otherwise it didn't work for me)
fig, ax= plt.subplots()
animation_canvas = False
prev_frame_time = 0

class Particles:
    def __init__(self):
        """
        Initialization of "group of particles" as a list of particles
        """
        self.par = []
        
    def add_par(self,par):
        """
        This method is used to add some particle
        """
        self.par.append(par)
      
    def destroy_particles(self):
        """
        This method is used to destroy all particles
        """
        self.par = []

    def print_par(self):
        """
        This method is used to print informations about all the particles
        """
        return(print(self.par))
    
    def innit_anim_on_canvas(self,x):
        """
        Initialization of animation on the canvas
        """
        global fig, animation_canvas
        animation_canvas = FigureCanvasTkAgg(figure = fig, master= x)
        animation_canvas.get_tk_widget().place(x = 500, y = 62, anchor="nw", height = 440, width = 440)
    
    def animation(self,x, save = False):
        """
        This method is used to create the simulation and plotting particles on the canvas in GUI
        """
        global fig, ax

        # Editing of the main surface on which the animation will take place.
        # So that it has the shape of a square and the desired properties.
        for s in ['top','bottom','left','right']:
            ax.spines[s].set_linewidth(2)
        ax.set_aspect('equal', 'box')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        fig.tight_layout(pad=0)

        # Ploting all those particles
        for p in self.par:
            p.plt_par(ax)
        
        def position_update(dt):
            """
            This function changes the position of the particles to which they move in time dt
            """
            for p in self.par:
                p.pos_x += dt * p.vel_x
                p.pos_y += dt * p.vel_y 

        def update(frame):
            """
            This function is used directly in the animation
            """
            global prev_frame_time

            current_time = frame * 0.001 # A value of 0.001 is chosen for animation smoothness
            dt = current_time - prev_frame_time
            prev_frame_time = current_time

            # Run functions that take care of collisions of  particles into walls and into each other
            bf.particles_bounce()
            bf.wall_bounce(self)

            # Change the velocity and position coordinantes also in the arrays         
            for p in particles.par:
                p.pos_coord = np.array((p.pos_x,p.pos_y))
                p.vel_coord = np.array((p.vel_x,p.vel_y))
            
            # Updage positions of all these particles according to changed velocities
            position_update(dt)

            # Change the position of all particles plots
            for p in self.par:
                p.point.set_data([p.pos_x],[p.pos_y])
            
            return

        if save == True:
            pass #possible to add function to save the animation
        else:
            
            # Animation of particles using function update 
            ani = FuncAnimation(fig, update, interval=1, cache_frame_data=False)

            # We have to loop the tkinter GUI
            x.mainloop()


particles = Particles()

def add_par(x,y,vx,vy,r,m):
    """
    This function is created just to test the simulation.
    It helps us to add particle to the simulation in easier way
    """
    particles.add_par(Particle(x,y,vx,vy,r,m))
