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
    if death > 0 and death < 9:
        alerta_1()
    elif death > 9 and death < 19:
        alerta_2()
    elif death > 19 and death < 29:
        alerta_3()
    elif death > 29:
        alerta_4()

def tigresa_oriente():
    sense.set_pixel(0, 0, 245, 0, 135)
    sense.set_pixel(7, 7, 245, 0, 135)
    sense.set_pixel(7, 0, 245, 0, 135)
    sense.set_pixel(0, 7, 245, 0, 135)
    death = 0
    old_degs = sense.get_orientation_degrees()
    while True:
        new_degs = sense.get_orientation_degrees()
        yaw=abs(abs(new_degs['yaw'])-abs(old_degs['yaw']))
        pitch=abs(abs(new_degs['pitch'])-abs(old_degs['pitch']))
        roll=abs(abs(new_degs['roll'])-abs(old_degs['roll']))
        for event in sense.stick.get_events():
            if event.action == "released" and event.direction != 'middle':
                exit()
        if yaw >.04 and yaw < 180:
            death +=1
            death_check(death)
        elif pitch >.04 and pitch < 180:
            death +=1
            death_check(death)
        elif roll >.04 and roll < 180:
            death +=1
            death_check(death)
        else:
            if death > 3:
                death = death-3
            elif death < 3:
                death = 0
                sense.clear()
        
        old_degs = new_degs

tigresa_oriente()