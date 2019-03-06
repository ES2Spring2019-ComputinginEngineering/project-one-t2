#Tina Guo and Amma Agyei
import os


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




