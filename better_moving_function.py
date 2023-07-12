import numpy as np
from easing import easing
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

index = count()

def animate(i):
   var = next(index)
   v = var*0.05 % 10
   plt.cla()
   plt.xlim(0,10)
   plt.ylim(0,10)
   plt.scatter(v,v)

ani = FuncAnimation(plt.gcf(), animate, frames = index, interval = 1)
plt.tight_layout()
plt.show()

