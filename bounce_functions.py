from itertools import combinations
import numpy as np

def wall_bounce(particles):
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
      if (a.radius + b.radius - 0.1)**2 > (a.pos_x - b.pos_x)**2 + (a.pos_y - b.pos_y)**2:
            return True
      else:
            return False

pairs = []
def pairs_of_particles(particles):
    global pairs
    pairs = list(combinations(particles, 2))
    return pairs


def particles_bounce():
    for a,b in pairs:
            if collision_check(a,b):
                X = 2 * np.dot(np.subtract(a.vel_coord,b.vel_coord), np.subtract(a.pos_coord, b.pos_coord))/(np.linalg.norm(a.pos_coord - b.pos_coord)**2 * (a.mass + b.mass))
                a.vel_coord = np.subtract(a.vel_coord, b.mass * X * np.subtract(a.pos_coord,b.pos_coord))
                b.vel_coord = np.subtract(b.vel_coord, a.mass * X * np.subtract(b.pos_coord,a.pos_coord))
                
                print(a)
                print(b)
                print(np.linalg.norm(a.pos_coord - b.pos_coord))

                a.vel_x = a.vel_coord[0]
                a.vel_y = a.vel_coord[1]
                b.vel_x = b.vel_coord[0]
                b.vel_y = b.vel_coord[1]
                a.pos_x = a.pos_x + a.vel_x * 0.002
                a.pos_y = a.pos_y + a.vel_y * 0.002
                b.pos_x = b.pos_x + b.vel_x * 0.002
                b.pos_y = b.pos_y + b.vel_y * 0.002
            else:
                pass
    return

