# pendulum project
# Amma Agyei and Tina Guo

#model a pendulum using legos and microbit
#use physics equations to determine period(T) and angular velocity(v)

import math
import numpy as np

L = .12 #m
g = 9.8 #m/s^2
m = 0.5 #kg
theta_max = 90 #degrees
theta = 172
theta_r = math.radians(theta)

def system_update(T, acc_t, vel_t, theta, t1, t2):
    #return updated values of period, acceleration, ang velocity, angular position
    dt = t2 - t1
    T = (2 * math.pi) * (math.sqrt(L / g))
    theta = theta_max * (math.sin( math.sqrt(g / L))) * dt
    acc_t = (g * math.sin(math.radians(theta))) /
    vel_t = math.sqrt(2 * g * L * (1 - (math.cos(theta_r))))
    return theta, vel_t, acc_t


def print_system(T, acc_t, vel_t, theta):
    print("TIME:        ", T)
    print("POSITION:    ", theta)
    print("VELOCITY:    ", vel_t)
    print("ACCEL:       ", acc_t,  "\n")


#initial conditions
theta_max = [0]
vel_t = [0]
acc_t = [0, 4.9, 6.9, 8.49, 9.8, 9.8, 8.49, 6.9, 4.9, 0, -4.9, -6.9, -8.49, -9.8, -9.8, -8.49, -6.9, -4.9, 0]
T = np.linspace(0, 20, 21)
print_system(T[0], theta[0], vel_t[0], acc_t[0])

i = 1
while i < len(T):
    theta, vel_t = system_update(acc_t[i], theta[i-1], vel_t[i-1], T[i-1], T[i])
    theta.append(theta)
    vel_t.append(vel_t)
    print_system(T[i], theta[i], vel_t[i])
    i += 1
