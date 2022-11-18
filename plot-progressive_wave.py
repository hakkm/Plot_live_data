import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np 
from itertools import count
from time import time

plt.style.use("fivethirtyeight")

max_x = 2000
x = np.arange(-max_x, max_x, 0.1)

# 24 frame per second (=smooth image) so the interval in FuncAnimation
# should be equal to the length of time
# in 5 seconds i have 5*24 frame
# 1/24 = 0.048 s
time = count(-5, 1/24) # start from -5s with interval = 1/24s

# each <interval> plot the u(x,t) with a fixed time 
# like for t in time: plot(x, u(x,t))
plt.figure(figsize=(10,4))
def animate(i):

    f1 = 1.3 # hz frequency
    f2 = 1.5 # hs frequency
    w1 = 2 * np.pi * f1   # pulsation
    w2 = 2 * np.pi * f2
    c = 340 # wave velocity , velocity independent of frequency
    k1 = w1/c   # wave vector 
    k2 = w2/c
    A = 3   # amplitude
    next_time = next(time)
    y_prog = A * np.cos(np.multiply(w1, np.array([next_time])) - np.multiply(k1,x))   # my psi function
    y_regr = A * np.cos(np.multiply(w2, np.array([next_time])) + np.multiply(k2,x))


    plt.cla() # clear the current axes
    ax = plt.gca()
    ax.set_ylim(-10, 10)

    plt.plot(x, y_regr + y_prog)

ani = FuncAnimation(plt.gcf(),
                    animate,
                    interval=42)

plt.tight_layout()
plt.show()