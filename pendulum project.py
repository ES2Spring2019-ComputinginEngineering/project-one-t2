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


def system_update(omega_initial, theta_initial, theta_t, time1, time2):
    #return updated values of period, acceleration, and velocity, angular position
    dt = time2 - time1
    theta = theta_initial + omega_initial * dt
    acc_initial = (-g / L * math.sin(omega_initial) )
    omega = omega_initial + acc_initial * dt
    acc_t = ((-1 * g) / L ) * math.sin(theta)
    return theta, acc_t, omega

def print_system(time, omega_initial, acc_initial, theta_initial):
    print("TIME:       ", time)
    print("POSITION:   ", theta_initial)
    print("ACCELERATION:   ", acc_initial)
    print("VELOCITY: ", omega_initial, "\n")
    print((time, theta_initial, acc_initial, omega_initial))

#initial conditions
theta_initial = [math.pi]
omega_initial = [0]
acc_initial = [0]
time = np.linspace(0, 20, 100)
print_system(time[0], omega_initial[0], acc_initial[0], theta_initial[0])

i = 1
while i < len(time):
    acc_t, theta, omega = system_update(omega_initial[i-1], theta_initial[i-1], acc_initial[i-1], time[i-1], time[i])
    omega_initial.append(omega)
    theta_initial.append(theta)
    acc_initial.append(acc_t)
    print_system(time[i], omega_initial[i], acc_initial[i], theta_initial[i])
    i += 1