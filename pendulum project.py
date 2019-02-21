# pendulum project
# Amma Agyei and Tina Guo

#model a pendulum using legos and microbit
#use physics equations to determine period(T) and angular velocity(v)

import math
import numpy as np

L = .12 #m
g = 9.8 #m/s^2
m = 0.5 #kg
w = math.sqrt(g / L)

def system_update(x_initial, omega_initial, time1, time2):
    #return updated values of period, acceleration, and velocity, angular position
    dt = time2 - time1
    T = (2 * np.pi) * (np.sqrt(L / g))
    omega = omega_initial * math.cos(math.sqrt(g / L) * dt )
    x_t = array_x * (np.sin(omega_initial * dt))
    #vel_t = omega_initial * w * math.cos( w * t)
    #acc_t = - omega_initial * w * math.sin( w * t)
    return x_t, omega

def print_system(time, x_initial, omega_initial):
    print("TIME:       ", time)
    print("POSITION:   ", x_initial)
    print("ANGLE:   ", omega_initial,  "\n")

#initial conditions
x_initial = [math.pi]
array_x = np.array(x_initial)
omega_initial = [0, math.pi/2, 20, 30, 40, math.pi / 3, math.pi / 4, math.pi / 6, math.pi, -math.pi, math.pi /2]
time = np.linspace(0, 20, 21)
print_system(time[0], x_initial[0], omega_initial[0])

i = 1
while i < len(time):
    x_t, omega = system_update(x_initial[i-1], omega_initial[i-1], time[i-1], time[i])
    x_initial.append(x_t)
    omega_initial.append(omega)
    print_system(time[i], x_initial[i], omega_initial[i])
    i += 1