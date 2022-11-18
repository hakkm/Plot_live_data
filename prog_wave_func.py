import numpy as np 

class ProgressiveWave:
    def __init__(self, time, x, freq=1, amplitude=1, c=340):
        
# def prog_wave_func(time, x, freq=1, amplitude=1, c=340, ):
#     f1 = 1.3 # hz frequency
#     w1 = 2 * np.pi * f1   # pulsation
#     c = 340 # wave velocity , velocity independent of frequency
#     k1 = w1/c   # wave vector 
#     A = 3   # amplitude
#     next_time = next(time)
#     y_prog = A * np.cos(np.multiply(w1, np.array([next_time])) - np.multiply(k1,x))
#     return y_prog