#Tina Guo and Amma Agyei
import os


fin = open('/Users/ammaagyei/mu_code/Experiment1.txt')  #Opens saved file
mytxt = fin.read()                                      #Reads saved file
print(mytxt)
t = []
acc = []
ang = []
i = 0
line = ""
data = []


for char in mytxt:
    if char == "\n":                     #Checks for the new line character, and appends the data
        data.append(line)
        line = ""
    else:
        line = line + char
for num in data:
    if i % 2 == 0:                      #if line is even, appends t list with the data
        t.append(float(num))
    else:                                      #if line is odd, appends splits odd line into acc list and ang list
        acc.append(float(num.split(",")[0]))
        ang.append(float(num.split(",")[1]))

    i += 1
fin.close()



