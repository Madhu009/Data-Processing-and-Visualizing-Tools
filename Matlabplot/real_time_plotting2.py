import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np


def init_animation():
    global line
    line, = ax.plot(x, np.zeros_like(x))
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1,1)

def animate(i):
    line.set_ydata(np.sin(2*np.pi*i / 50)*np.sin(x))
    return line,

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(0, 2*np.pi, 200)

ani = matplotlib.animation.FuncAnimation(fig, animate, init_func=init_animation, frames=50)
ani.save('/tmp/animation.mp4', writer='imagemagick', fps=30)