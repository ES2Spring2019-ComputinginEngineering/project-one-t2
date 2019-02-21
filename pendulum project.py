# pendulum project
# Amma Agyei and Tina Guo

#model a pendulum using legos and microbit
#use physics equations to determine period(T) and angular velocity(v)

import math
import numpy as np

L = .12 #m
g = 9.8 #m/s^2
m = 0.5 #kg
time = np.linspace(0, 20, 21)


def system_update(x_initial, time1, time2):
    #return updated values of period, acceleration, ang velocity, angular position
    T = (2 * math.pi) * (math.sqrt(L / g))
    omega = (2 * math.pi) / T
    x_t = x_initial * math.sin(omega * time)
    #acc_t = (g * math.sin(math.radians(theta))) / m
    #vel_t = math.sqrt(2 * g * L * (1 - (math.cos(theta_r))))
    return T, x_t #theta, vel_t, acc_t


def print_system(time, x_t):#, acc_t, vel_t, theta):
    print("TIME:          ", time)
    print("POSITION:    ", x_t, "\n")
    #print("VELOCITY:    ", vel_t)
    #print("ACCEL:       ", acc_t,  "\n")


#initial conditions
x_initial = [0]
#vel_t = [0]
#acc_t = [0, 4.9, 6.9, 8.49, 9.8, 9.8, 8.49, 6.9, 4.9, 0, -4.9, -6.9, -8.49, -9.8, -9.8, -8.49, -6.9, -4.9, 0]

print_system(time[0], x_initial[0]) #theta[0], vel_t[0], acc_t[0])

i = 1
while i < len(time):
    x_t = system_update(x_initial[i-1],  time[i-1], time[i])
    x_initial.append(x_t)
    print_system(time[i], x_initial[i])#, theta[i], vel_t[i])
    i += 1
