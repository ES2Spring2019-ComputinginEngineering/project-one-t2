import microbit
import math

#Pseudocode
#Calculate angle function
#Stop watch function to know angle after a certain amount of time.
#Be able to log time data with position data that is, as the position of microbit is changing, record the angle and the time at that angle.
#Statement to begin logging of data, and statement to end logging of data.
#Speed of at least 10Hz

import os

#Comma-Separated Values

time0 = 0
time1 = 0
elapsed_time = time1 - time0

def calculate_angle(x,y,z):
        a1 = math.atan2(x, math.sqrt((y**2) + (z**2 )))
        return math.degrees(a1)


while True:
    if microbit.button_a.was_pressed():
        with open('time_and_angle_data.txt', 'w') as my_file:
            while not microbit.button_b.was_pressed():
                microbit.display.show(microbit.Image.ARROW_E)
                time0 = microbit.running_time()
                x = microbit.accelerometer.get_x()
                y = microbit.accelerometer.get_y()
                z = microbit.accelerometer.get_z()
                x_angle = calculate_angle(x, y, z)
                y_angle = calculate_angle(y, x, z)
                print(time0)
                print(y_angle)
                my_file.write(str(time0) + "\n")
                my_file.write(str(y_angle) + "\n")





