from sense_hat import SenseHat
sense = SenseHat()
from datetime import datetime
import time

sense.low_light = True

def alerta_1():
    X = [245, 0, 135]  # pink
    O = [0, 0, 0]  # nothing
    sense.set_pixels([
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ])

def alerta_2():
    X = [245, 0, 135]  # pink
    O = [0, 0, 0]  # nothing
    sense.set_pixels([
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ])

def alerta_3():
    X = [245, 0, 135]  # pink
    O = [0, 0, 0]  # nothing
    sense.set_pixels([
    O, O, O, O, O, O, O, O,
    O, X, X, X, X, X, X, O,
    O, X, X, X, X, X, X, O,
    O, X, X, X, X, X, X, O,
    O, X, X, X, X, X, X, O,
    O, X, X, X, X, X, X, O,
    O, X, X, X, X, X, X, O,
    O, O, O, O, O, O, O, O
    ])


def alerta_4():
    sense.clear(245, 0, 135)

def death_check(death):
    if death == 0:
        sense.clear()
    elif death > 0 and death < 29:
        alerta_1()
    elif death > 29 and death < 59:
        alerta_2()
    elif death > 59 and death < 99:
        alerta_3()
    elif death > 99:
        alerta_4()

def tigresa_oriente():
    sense.set_pixel(0, 0, 245, 0, 135)
    sense.set_pixel(7, 7, 245, 0, 135)
    sense.set_pixel(7, 0, 245, 0, 135)
    sense.set_pixel(0, 7, 245, 0, 135)
    death = int(0)
    old_degs = sense.get_orientation_degrees()
    while True:
        new_degs = sense.get_orientation_degrees()
        yaw=abs(abs(new_degs['yaw'])-abs(old_degs['yaw']))
        pitch=abs(abs(new_degs['pitch'])-abs(old_degs['pitch']))
        roll=abs(abs(new_degs['roll'])-abs(old_degs['roll']))
        for event in sense.stick.get_events():
            if event.action == "released" and event.direction != 'middle':
                exit()
        if yaw >.05 and yaw < 180:
            death +=1
        elif pitch >.05 and pitch < 180:
            death +=1
        elif roll >.05 and roll < 180:
            death +=1
        else:
            if death >= 2:
                death -=2
            elif death < 2:
                death = 0
        death_check(death)
        old_degs = new_degs

tigresa_oriente()
