# pendulum project
# Amma Agyei and Tina Guo

#Import Statements
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.signal as sig


#Global Variables
L = 0.56 #m
g = -9.8 #m/s^2
m = 0.5 #kg

#Functions
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
time = np.linspace(0, 20, 100000)
print_system(omega_initial[0], acc_initial[0], theta_initial[0])

i = 1
while i < len(time):
    theta, acc_t, omega = system_update(omega_initial[i-1], theta_initial[i-1], acc_initial[i-1], time[i-1], time[i])
    omega_initial.append(omega)
    theta_initial.append(theta)
    acc_initial.append(acc_t)
    i += 1


#Plots acceleration vs time on graph
plt.figure(1)
plt.subplot(3,1,2)
plt.plot(time,acc_initial, 'k-')
plt.xlabel('Time(seconds)')
plt.ylabel('acceleration(m/s**2)')
plt.title('Acceleration vs Time')
plt.xlim((0,20))
plt.grid()


#Plots velocity vs time on graph
plt.figure(2)
plt.subplot(3,1,2)
plt.plot(time,omega_initial, 'k-')
plt.xlabel('Time(seconds)')
plt.ylabel('velocity(m/s)')
plt.title('Velocity vs Time')
plt.xlim((0,20))
plt.grid()


#Plots position vs time on graph
plt.figure(3)
plt.subplot(3,1,2)
plt.plot(time,theta_initial, 'k-')
plt.xlabel('Time(seconds)')
plt.ylabel('position(m)')
plt.title('Position vs Time')
plt.xlim((0,20))
plt.grid()


#finding peaks
theta_initial = np.radians(theta_initial)   
acc_initial = np.array(acc_initial)
t = np.array(time)
t = t

acc_pks,_ = sig.find_peaks(acc_initial,2,3,10)
acc_filt = sig.medfilt(acc_initial,5)
acc_filt_pks, _ = sig.find_peaks(acc_filt,1,None,7)

plt.figure()
plt.plot(t,acc_initial, 'r-', t[acc_pks],acc_initial[acc_pks], 'b.')
plt.xlabel('Time(seconds)')
plt.ylabel('acceleration(m/s**2)')
plt.title('Noisy Data')
plt.show()

plt.figure()
plt.plot(t, acc_filt, 'r-',t[acc_filt_pks],acc_filt[acc_filt_pks], 'b.')
plt.xlabel('Time(seconds)')
plt.ylabel('acceleration(m/s**2)')
plt.title('Filtered Data')
plt.show()

plt.figure()
plt.plot(t, acc_filt, 'r-',t[acc_filt_pks],acc_filt[acc_filt_pks], 'b.')
plt.xlabel('Time(seconds)')
plt.ylabel('acceleration(m/s**2)')
plt.title('Filtered Data')
plt.show()

newt = t[acc_filt_pks]
newacc = acc_initial[acc_filt_pks]

t.resize((17,),refcheck = False)
plt.figure()
plt.plot(newt, newacc, 'ro-')
plt.xlabel('Time(seconds)')
plt.ylabel('acceleration(m/s**2)')
plt.title('Peaks Vs Time')
plt.show()


mean_Period = newt.mean()
print(mean_Period)