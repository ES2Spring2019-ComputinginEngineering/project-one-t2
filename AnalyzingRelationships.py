#Import statement
import matplotlib.pyplot as plt



# Real Time Data 
T = [4357,4358,4649,5000,7205]    #period data acquired from 5 real world data experiments 
L = [0.29,0.35,0.42,0.48,0.59]    #length of pendulum in metres for 5 real world data experiments

#Simulation Data
T= [9.67,9.85,9.956,9.99,10.1]
L = [0.29,0.35,0.42,0.48,0.59]

#Plotting Relationship beteen length and period for real world data
plt.figure()
plt.title('Relationship between pendulum length and Period for Real World Data')
plt.yscale('log')
plt.xlabel('Length')
plt.ylabel('Period')
plt.xscale('log')
plt.plot(L, T, 'k-')
plt.grid(True)


#Plotting Relationship between length and period for simulation data
plt.figure()
plt.title('Relationship between pendulum length and Period for Simulation Data')
plt.xlabel('Length')
plt.ylabel('Period')
plt.yscale('log')
plt.xscale('log')
plt.plot(L, T, 'k-')
plt.grid(True)


