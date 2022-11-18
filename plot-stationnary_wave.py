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

    f = 100 # hz frequency
    w = 2 * np.pi * f   # pulsation
    c = 340 # wave velocity , velocity independent of frequency
    k = w/c   # wave vector 
    A_g = 3 # amplitude de g
    phi_g = 0   # phase a l'origine de g
    psi_f = 0   # phase a l'origine de f
    B_f = 3 # amplitude de f  

    plt.cla() # clear the current axes ie erase the recent plot from the figure so it will be empty for new plotting
    # try limit y axis to 8 for instance
    ax = plt.gca()
    ax.set_ylim(-10, 10)


    g_of_t = A_g * np.cos(np.multiply(w, np.array([next_time])) + phi_g)    # Acos(wt + phi_g)
    f_of_x = B_f * np.cos(np.multiply(k, x) + psi_f) # Bcos(kx + psi)

    plt.plot(x, g_of_t * f_of_x, '-g')

    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),
                    animate,
                    interval=10)

plt.tight_layout()
plt.show()