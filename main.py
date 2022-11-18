import matplotlib.pyplot as plt 
from itertools import count 
from matplotlib.animation import FuncAnimation
import random 

plt.style.use("fivethirtyeight")

x_vals = []
y_vals = []

index = count() # counts up one number at a time and give the next number at a time

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 4))
    plt.cla() # else each <interval> plot with diffrent color
    plt.plot(x_vals, y_vals )


# call at each <interval> the animate the function
ani = FuncAnimation(plt.gcf(), # get current figure, you put the figure 
                    animate,
                    interval=1000 # ms
                    )   

plt.tight_layout() # add automatic padding
plt.show()