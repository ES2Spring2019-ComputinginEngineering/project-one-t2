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
    acc_t = (g * math.sin(math.radians(theta))) / m
    vel_t = math.sqrt(2 * g * L * (1 - (math.cos(theta_r))))


def update_system(T, acc_t, vel_ t, theta):
    print("TIME:        ", T)
    print("POSITION:    ", theta)
    print("VELOCITY:    ", vel_t,  "\n")


    #initial conditions
theta = [0]
vel_t = [0]
acc_t = [0, 4.9, 6.9, 8.49, 9.8, 9.8, 8.49, 6.9, 4.9, 0,
