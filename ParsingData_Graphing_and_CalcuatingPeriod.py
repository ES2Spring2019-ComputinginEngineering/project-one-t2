import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig


fin = open('/Users/ammaagyei/mu_code/Experiment1.txt')
mytxt = fin.read()
print(mytxt)
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

plt.figure(figsize=(8,8))
plt.subplot(3,1,2)
plt.plot(t, acc, 'k-')
plt.xlim(900,8500)
plt.ylim(-500,200)
plt.xlabel('Time(milliseconds)')
plt.ylabel('acceleration(m/s**2)')
plt.title("Acceleration vs Time")
plt.grid()

plt.figure(figsize=(8,8))
plt.subplot(3,1,2)
plt.plot(t, ang, 'k-')
plt.xlabel('Time(milliseconds)')
plt.ylabel('angle(radians))')
plt.xlim(4500,7000)
plt.ylim(-8,2)
plt.title("Theta vs Time")
plt.grid()

ang = np.radians(ang)   
acc = np.array(acc)
t = np.array(t)
acc_filt = sig.medfilt(acc,33)
acc_pks,_ = sig.find_peaks(acc,10)
acc_filt_pks, _ = sig.find_peaks(acc_filt,None,None)

plt.figure()
plt.plot(t,acc, 'r-', t[acc_pks],acc[acc_pks], 'b.')
plt.title('Noisy Data')
plt.show()

plt.figure(figsize=(10,10))
plt.plot(t, acc_filt, 'r-',t[acc_filt_pks],acc_filt[acc_filt_pks], 'b.')
plt.title('Filtered Data')
plt.show()

t.resize((12,),refcheck = False)
plt.figure()
plt.plot(t, acc_filt_pks, 'ro-')
plt.title('Peaks Vs Time')
plt.show()


mean_T = acc_filt_pks.mean()  #Period
T = mean_T
