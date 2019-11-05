# -*- coding: utf-8 -*-
# from sys import argv
# soy_un_argumentvariable = argv
from sense_hat import SenseHat
import time
from datetime import datetime
sense = SenseHat()
##
old_degs = sense.get_orientation_degrees()
death = [0,0,0]
while True:
    new_degs = sense.get_orientation_degrees()
    yaw=abs(abs(new_degs['yaw'])-abs(old_degs['yaw']))
    pitch=abs(abs(new_degs['pitch'])-abs(old_degs['pitch']))
    roll=abs(abs(new_degs['roll'])-abs(old_degs['roll']))
    if yaw >.04 and yaw < 180:
        # print ("YAW",datetime.now(), yaw)
        death[0] += 1
    elif pitch >.04 and pitch < 180:
        # print ("PIT",datetime.now(), pitch)
        death[1] += 1
    elif roll >.04 and roll < 180:
        # print ("ROL",datetime.now(), roll)
        death[2] += 1
    else:
        for i in range(len(death)):
            if death[i] > 0:
                death[i]=death[i]-1
#     if death > 10: print(datetime.now())
    print(death)
    #print (f"death count = {death}")
    old_degs = new_degs
    time.sleep(.01)
##
# sense.set_imu_config(False, False, True)
# while True: print(sense.accelerometer)
##
# print("roll,pitch,yaw")
# while True:
#     degs = sense.get_orientation_degrees()
#     print(f"{degs['roll']},{degs['pitch']},{degs['yaw']}")
#     time.sleep(.1)
##
# print("roll,pitch,yaw")
# for ass in range (0,6000):
#     degs = sense.get_orientation_degrees()
#     print(f"{degs['roll']},{degs['pitch']},{degs['yaw']}")
#     time.sleep(.1)
#     ass +=1
# ##
# while True:
#     elaccel = sense.accelerometer_raw
#     if elaccel['x']>1:
#         print ("x", elaccel['x'])
#     elif elaccel['y']>1:
#         print ("y", elaccel['y'])
#     elif elaccel['z']>1.02:
#         print ("z", elaccel['z'])
##
# while True:
#     elaccel = sense.accelerometer
#     if elaccel['roll']>1:
#         print ("roll", elaccel['roll'])
#     elif elaccel['pitch']>1:
#         print ("pitch", elaccel['pitch'])
#     elif elaccel['yaw']>1:
#         print ("yaw", elaccel['yaw'])

# while True:
#     baby = sense.get_gyroscope()
#     print(f"{round(baby['roll'],2)}\t {round(baby['pitch'],2)}\t {round(baby['yaw'],2)}")
