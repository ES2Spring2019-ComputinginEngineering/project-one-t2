#Amma Agyei and Tina Guo
#Data Logging

#Import statements
import microbit
import math

#Global variable
time0 = 0


#A function to calculate the angle in degrees
def calculate_angle(x,y,z):
        a1 = math.atan2(x, math.sqrt((y**2) + (z**2 )))
        return math.degrees(a1)


#When microbit button a is pressed, microbit begins logging data and writing the data to the file opened.When microbit button b is pressed, microbit stops collecting data.
while True:
    if microbit.button_a.was_pressed():
        with open('Experiment1.txt', 'w') as my_file:
            while not microbit.button_b.was_pressed():
                microbit.display.show(microbit.Image.ARROW_E)   #indicates when microbit is logging data
                time0 = microbit.running_time()
                x = microbit.accelerometer.get_x()
                y = microbit.accelerometer.get_y()
                z = microbit.accelerometer.get_z()
                x_angle = calculate_angle(x, y, z)
                y_angle = calculate_angle(y, x, z)
                print(time0)
                print(y_angle)
                my_file.write(str(time0) + "\n")                  #writes time onto opened file
                my_file.write(str(y)+ "," + str(y_angle) + "\n")  #writes acceleration on y axis and angle calculated based on this acceleration onto the file opened.

