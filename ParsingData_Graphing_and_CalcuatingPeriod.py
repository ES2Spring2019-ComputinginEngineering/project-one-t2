import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

#Opening file containing experiment data
fin = open('/Users/ammaagyei/mu_code/Experiment1.txt')
mytxt = fin.read()
print(mytxt)


#Splitting data on file into acceleration list, angular position list and time list
t = []
acc = []
ang = []
i = 0
line = ""
data = []
for char in mytxt:
    if char == "\n":
        data.append(line)
        line = ""
    else:
        line = line + char
for num in data:
    if i % 2 == 0:
        t.append(float(num))
    else:
        acc.append(float(num.split(",")[0]))
        ang.append(float(num.split(",")[1]))
        
    i += 1
fin.close()

#Plotting Acceleration vs Time
plt.figure(figsize=(8,8))
plt.subplot(3,1,2)
plt.plot(t, acc, 'k-')
plt.xlim(900,8500)
plt.ylim(-500,200)
plt.xlabel('Time(milliseconds)')
plt.ylabel('acceleration(m/s**2)')
plt.title("Acceleration vs Time")
plt.grid()


#Plotting Angle vs Time
plt.figure(figsize=(8,8))
plt.subplot(3,1,2)
plt.plot(t, ang, 'k-')
plt.xlabel('Time(milliseconds)')
plt.ylabel('angle(radians))')
plt.xlim(4500,7000)
plt.ylim(-8,2)
plt.title("Theta vs Time")
plt.grid()


#Graphing filtered data and finding peaks
ang = np.radians(ang)   
acc = np.array(acc)
t = np.array(t)
acc_filt = sig.medfilt(acc,33)
acc_pks,_ = sig.find_peaks(acc,10,prominence=200)
acc_filt_pks, _ = sig.find_peaks(acc_filt,None,None)

#Plotting Noisy Data
plt.figure()
plt.plot(t,acc, 'r-', t[acc_pks],acc[acc_pks], 'b.')
plt.title('Noisy Data')
plt.show()

#Plotting Filtered Data
plt.figure(figsize=(10,10))
plt.plot(t, acc_filt, 'r-',t[acc_filt_pks],acc_filt[acc_filt_pks], 'b.')
plt.title('Filtered Data')
plt.show()


#Plotting Peaks vs Time and Calculating the Period
newt = t[acc_filt_pks]
newacc= acc[acc_filt_pks]
t.resize((9,),refcheck = False)
plt.figure()
plt.plot(newt, newacc, 'ro-')
plt.title('Peaks Vs Time')
plt.show()

#Calculating the period
mean_T = newt.mean() 
T = mean_T
