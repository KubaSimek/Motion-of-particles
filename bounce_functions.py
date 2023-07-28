from itertools import combinations
import numpy as np

def wall_bounce(particles):
        for p in particles.par:
            if (0 + p.radius/50) > p.pos_x:
                    p.pos_x = p.radius/50
                    p.vel_x = -p.vel_x
            if (10 - p.radius/50) < p.pos_x:
                    p.pos_x = 10 - p.radius/50
                    p.vel_x = -p.vel_x
            if (0 + p.radius/50) > p.pos_y:
                    p.vel_y = -p.vel_y
                    p.pos_y = p.radius/50
            if (10 - p.radius/50) < p.pos_y:
                    p.pos_y = 10 - p.radius/50
                    p.vel_y = -p.vel_y
        return

def collision_check(a,b):
      if (a.radius/50 + b.radius/50)**2 >= (a.pos_x - b.pos_x)**2 + (a.pos_y - b.pos_y)**2:
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

                """"
                m1, m2 = a.radius, b.radius

                n = np.array((a.pos_x - b.pos_x, a.pos_y - b.pos_y))
                t = np.array((a.pos_y - b.pos_y, b.pos_x - a.pos_x))
                matrix = np.array([n,t])

                vel_a_nt = np.array(((m1-m2)/(m1+m2))* np.dot(a.vel_coord,n),np.dot(a.vel_coord,t))
                vel_b_nt = np.array(np.dot(b.vel_coord,n) + (m1/(m1+m2))*2* np.dot(a.vel_coord,n),np.dot(b.vel_coord,t))

                x_nt = np.dot(np.invert(matrix),vel_a_nt)
                y_nt = np.dot(np.invert(matrix),vel_b_nt)

                vel_a_xy = np.array((np.dot(vel_a_nt,x_nt),np.dot(vel_a_nt,y_nt)))
                vel_b_xy = np.array((np.dot(vel_b_nt,x_nt),np.dot(vel_b_nt,y_nt)))

                a.vel_x = vel_a_xy[0]
                a.vel_y = vel_a_xy[1]
                b.vel_x = vel_b_xy[0]
                b.vel_y = vel_b_xy[1]
                """
                m1, m2 = a.radius**2, b.radius**2
                M = m1 + m2
                r1, r2 = a.pos_coord, b.pos_coord
                d = np.linalg.norm(r1 - r2)**2
                v1, v2 = a.vel_coord, b.vel_coord
                u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
                u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
                a.vel_x = u1[0]
                a.vel_y = u1[1]
                b.vel_x = u2[0]
                b.vel_y = u2[1]

          else:
                pass
    return

