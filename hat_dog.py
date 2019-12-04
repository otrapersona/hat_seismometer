from sense_hat import SenseHat
sense = SenseHat()
from datetime import datetime
import time
import light

def fourth():
    X = [245, 0, 135]  # pink
    O = [0, 0, 0]  # nothing
    sense.set_pixels([
    X, X, X, X, X, X, X, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, X, X, X, X, X, X, X
    ])

def third():
    X = [245, 0, 135]  # pink
    O = [0, 0, 0]  # nothing
    sense.set_pixels([
    O, O, O, O, O, O, O, O,
    O, X, X, X, X, X, X, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, X, X, X, X, X, X, O,
    O, O, O, O, O, O, O, O
    ])

def second():
    X = [245, 0, 135]  # pink
    O = [0, 0, 0]  # nothing
    sense.set_pixels([
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ])

def first():
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

def byeFelicia():
    fourth()
    time.sleep(.1)
    third()
    time.sleep(.1)
    second()
    time.sleep(.1)
    first()
    time.sleep(.1)
    sense.clear()

def hellobaby():
    first()
    time.sleep(.1)
    second()
    time.sleep(.1)
    third()
    time.sleep(.1)
    fourth()
    time.sleep(.1)
    sense.clear()

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
    elif 19 < death < 39:
        alerta_1()
    elif 39 < death < 59:
        alerta_2()
    elif 59 < death < 79:
        alerta_3()
    elif death > 99:
        alerta_4()

def tigresa_oriente():
    light.reader()
    hellobaby()
    death = int(0)
    old_degs = sense.get_orientation_degrees()
    while True:
        new_degs = sense.get_orientation_degrees()
        yaw=abs(abs(new_degs['yaw'])-abs(old_degs['yaw']))
        if yaw > 180:
            yaw = abs(yaw - 360)
        pitch=abs(abs(new_degs['pitch'])-abs(old_degs['pitch']))
        if pitch > 180:
            pitch = abs(pitch - 360)
        roll=abs(abs(new_degs['roll'])-abs(old_degs['roll']))
        if roll > 180:
            roll = abs(roll - 360)
        for event in sense.stick.get_events():
            if event.action != "idontcare" and event.direction != "middle":
                byeFelicia()
                exit()
        if .8 < yaw < 180:
            death +=1
        elif .05 < pitch < 180:
            death +=1
        elif .2 < roll < 180:
            death +=1
        else:
            if death >= 2:
                death -=2
            elif death < 2:
                death = 0
        death_check(death)
        old_degs = new_degs

tigresa_oriente()
