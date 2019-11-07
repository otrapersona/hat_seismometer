from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
event = sense.stick.wait_for_event()

def wait_4_joy():
    rejoice = sense.stick.wait_for_event().action
    if rejoice == 'pressed' or rejoice == 'released':
        print("my wife")
    elif sense.stick.wait_for_event().action == 'held':
        exit()

while True:
    wait_4_joy()