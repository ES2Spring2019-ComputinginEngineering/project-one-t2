#Tina Guo and Amma Agyei
import os

os

"""myfile = open('/Users/ammaagyei/mu_code/accelerometer0.txt')
mytxt = myfile.read()
myfile.close()
print(mytxt)
print(type(mytxt))"""


#i = 1
def time_and_angle_data():
    fin = open('/Users/ammaagyei/mu_code/accelerometer0.txt')
    mytxt = fin.read()
    print(mytxt)
    t = []
    a = []
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
        #num = data.strip()
        if i % 2 == 0:
            t.append(num)
        else:
            a.append(num)
        i += 1
    fin.close()
    #return a , t
    print("Angle=", a)
    print("Time=", t)


#Graph acceleration vs time:

#Plug in acceleration into



