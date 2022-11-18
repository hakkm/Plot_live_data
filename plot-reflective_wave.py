import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np 
from itertools import count
from time import time

plt.style.use("fivethirtyeight")

max_x = 1000
x = np.arange(-max_x, max_x, 0.1)

# 24 frame per second (=smooth image) so the interval in FuncAnimation
# should be equal to the length of time
# in 5 seconds i have 5*24 frame
# 1/24 = 0.048 s
time = count(-5, 0.01) # start from -5s with interval = 1/24s


# each <interval> plot the u(x,t) with a fixed time 
# like for t in time: plot(x, u(x,t))
plt.figure(figsize=(10,4))
def animate(i):
    next_time = next(time)

    f = 2 # hz frequency
    w = 2 * np.pi * f   # pulsation
    c = 340 # wave velocity , velocity independent of frequency
    k = w/c   # wave vector 
    psi_0 = 3 # amplitude de g
    L = 1   #  metre
 
    psi_i = psi_0 * np.cos(np.multiply(100*w, np.array([next_time])) - np.multiply(k, x))    # Acos(wt + phi_g)
    psi_r = -psi_0 * np.cos(np.multiply(k, x) + 2*k*L + np.multiply(2*w, np.array([next_time]))) # Bcos(kx + psi)

    plt.cla() # clear the current axes ie erase the recent plot from the figure so it will be empty for new plotting
    # try limit y axis to 8 for instance
    ax = plt.gca()
    ax.set_ylim(-10, 10)

    plt.plot(x, psi_r, '-g')

    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),
                    animate,
                    interval=10)

plt.tight_layout()
plt.show()