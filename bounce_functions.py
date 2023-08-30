"""
Python file with functions
These functions are used to simulate the change of velocities (in each direction) of particles when they touch the wall or each others
Also some function just helping to track and process these collisions
"""

from itertools import combinations
import numpy as np

def wall_bounce(particles):
    """
    This function is called from the Main_program.py

    This function checks if some particle is touching a wall (or is little bit "in a wall")
    and then change the sign of the velocity of the particle in corresponding direction. 
    For example if the particle touches the right wall, the velocity in the X direction should change the sign to "-" to simulate the collision.

    After the changing of the velicity, the corresponding position coordinant of the particle is set as the radius of the particle.
    This is how the program prevents bugs that could occur if a particle hits a wall at high speed and before the program records it,
    it would get further into the wall and when the speed changes, the program would record the collision again because the particle does not have time
    to leave the wall and therefore the particle would remain stuck in the wall
    """
    for p in particles.par:
        if (0 + p.radius) > p.pos_x:
            p.pos_x = p.radius
            p.vel_x = -p.vel_x
        if (10 - p.radius) < p.pos_x:
            p.pos_x = 10 - p.radius
            p.vel_x = -p.vel_x
        if (0 + p.radius) > p.pos_y:
            p.vel_y = -p.vel_y
            p.pos_y = p.radius
        if (10 - p.radius) < p.pos_y:
            p.pos_y = 10 - p.radius
            p.vel_y = -p.vel_y
    return

def collision_check(a,b):
    """
    This function checks if particles a and b are touching.
    It checks if the distance between the centers of these particles is smaller than the sum of the two radii using Pythagorean theorem
    """
    if (a.radius + b.radius)**2 > (a.pos_x - b.pos_x)**2 + (a.pos_y - b.pos_y)**2:
        return True
    else:
        return False

pairs = []
def pairs_of_particles(particles):
    """
    This function is called at the beginning of the program.

    This function creates all possible pairs of particles in the simulation.
    These pairs are stored in the global variable "pairs" and every time we want to check every possible collision of particles
    we can just iterate over this list. 
    """
    global pairs
    pairs = list(combinations(particles, 2))
    return pairs


def particles_bounce():
    """
    This function is called from Main_program.py

    This function iterate over the list of pairs of particles, checks if particles in the pair collide
    and then change the velocities of both particles to simulate the elastic collistion.

    After the changing of the velicities, particles are moved so they just touching again.(not intersect)
    We select one particle and move the second particle in the direction given by the straight line between the centers
    to the distance of the sum of both radii from the center of the second particle.
    It helps avoid the same bugs described in the function wall_bounce
    """
    for a,b in pairs:
            if collision_check(a,b):
                X = 2 * np.dot(np.subtract(a.vel_coord,b.vel_coord), np.subtract(a.pos_coord, b.pos_coord))/(np.linalg.norm(np.subtract(a.pos_coord, b.pos_coord))**2 * (a.mass + b.mass))
                a.vel_coord = np.subtract(a.vel_coord, b.mass * X * np.subtract(a.pos_coord,b.pos_coord))
                b.vel_coord = np.subtract(b.vel_coord, a.mass * X * np.subtract(b.pos_coord,a.pos_coord))
                
                print(a) #print just to check parametres of the particle
                print(b) #print just to check parametres of the particle

                a.vel_x = a.vel_coord[0]
                a.vel_y = a.vel_coord[1]
                b.vel_x = b.vel_coord[0]
                b.vel_y = b.vel_coord[1]

                line_1 = np.subtract(a.pos_coord, b.pos_coord)
                # We divide by the norm of this segment and scale to the distance of the radii
                line_norm = line_1 / np.linalg.norm(line_1) 
                line_2 = line_norm * (a.radius + b.radius)
                a.pos_x = b.pos_x + line_2[0]
                a.pos_y = b.pos_y + line_2[1]
            else:
                pass
    return

