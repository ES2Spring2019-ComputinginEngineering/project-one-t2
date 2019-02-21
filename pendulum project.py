# pendulum project
# Amma Agyei and Tina Guo

#model a pendulum using legos and microbit
#use physics equations to determine period(T) and angular velocity(v)

import math
import numpy as np
import time

L = .12 #m
g = 9.8 #m/s^2
m = 0.5 #kg
w = math.sqrt(g / L)

def system_update(x_initial, theta_initial, vel_t, time1, time2):
    #return updated values of period, acceleration, and velocity, angular position
    dt = time2 - time1
    T = (2 * np.pi) * (np.sqrt(L / g))
    theta = theta_initial * math.cos(math.sqrt(g / L) * dt )
    x_t = array_x * (np.sin(theta_initial * dt))

    if (theta_initial > 0):
        vel_t = w * x_initial * math.cos(w * dt)
    else:
        vel_t = -1 * w * x_initial * math.cos(w * dt)
    #vel_t = omega_initial * w * math.cos( w * t)
    #acc_t = - omega_initial * w * math.sin( w * t)
    return x_t, theta, vel_t

def print_system(time, x_initial,vel_t, theta_initial):
    print("TIME:       ", time)
    print("POSITION:   ", x_initial)
    print("ANGLE:   ", theta_initial)
    print("VELOCITY: ", vel_t, "\n")
    print((time, x_initial, vel_t, theta_initial))

#initial conditions
x_initial = [math.pi]
array_x = np.array(x_initial)
vel = [0]
theta_initial = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90,90,90,90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 0, 0]
time = np.linspace(0, 20, 21)
print_system(time[0], vel[0], x_initial[0], theta_initial[0])

i = 1
while i < len(time):
    x_t, theta, vel_t = system_update(x_initial[i-1], theta_initial[i-1], vel[i-1], time[i-1], time[i])
    x_initial.append(x_t)
    vel.append(vel_t)
    theta_initial.append(theta)
    print_system(time[i], x_initial[i], vel[i], theta_initial[i])
    i += 1

