import Main_program as mp
import easing as ea


tan = (mp.p1.vel_y)/(mp.p1.vel_x)

def line(t):
    return mp.np.array([mp.p1.pos_x + t * mp.p1.vel_x], [mp.p1.pos_y + t * mp.p1.vel_y])

def update2(t):
    x,y = line(t)
    mp.point.set_data([x], [y])
    return mp.point,

ani2 = mp.FuncAnimation(mp.fig, update2, interval = 1)

