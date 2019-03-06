# pendulum project
# Amma Agyei and Tina Guo

#model a pendulum using legos and microbit
#use physics equations to determine period(T) and angular velocity(v)

import math
import numpy as np
import matplotlib.pyplot as plt
import time

L = 1 #m
g = 9.8 #m/s^2
m = 0.5 #kg


def system_update(omega_initial, theta_initial, acc_initial, time1, time2):
    #return updated values of period, acceleration, and velocity, angular position
    dt = time2 - time1
    theta = theta_initial + omega_initial * dt
    omega = omega_initial + (acc_initial * dt)
    acc_t = ((-1 * g) / L ) * math.sin(theta)
    return theta, acc_t, omega

def print_system(omega_initial, acc_initial, theta_initial):
    print("POSITION:   ", theta_initial)
    print("ACCELERATION:   ", acc_initial)
    print("VELOCITY: ", omega_initial, "\n")
    print((omega_initial, acc_initial, theta_initial))

#initial conditions
theta_initial = [math.pi / 6]
omega_initial = [0]
acc_initial = [-4.9]
time = np.linspace(0, 20, 20000)
print_system(omega_initial[0], acc_initial[0], theta_initial[0])

i = 1
while i < len(time):
    theta, acc_t, omega = system_update(omega_initial[i-1], theta_initial[i-1], acc_initial[i-1], time[i-1], time[i])
    omega_initial.append(omega)
    theta_initial.append(theta)
    acc_initial.append(acc_t)
    #print_system(omega_initial[i], acc_initial[i], theta_initial[i])
    i += 1
    

plt.figure(figsize=(8,4),dpi=100)
plt.subplot(3,1,2)
plt.plot(time,acc_initial, 'ro--')
plt.xlabel('Time(seconds)')
plt.ylabel('acceleration(m/s**2)')
plt.xlim((0,20))
plt.grid()

plt.figure(2)
plt.subplot(3,1,2)
plt.plot(time,omega_initial, 'ro--')
plt.xlabel('Time(seconds)')
plt.ylabel('velocity(m/s)')
plt.xlim((0,20))
plt.grid()

plt.figure(3)
plt.subplot(3,1,2)
plt.plot(time,theta_initial, 'ro--')
plt.xlabel('Time(seconds)')
plt.ylabel('position(m)')
plt.xlim((0,20))
plt.grid()

