import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat
sense = SenseHat

def debugo(t):
    file=open("luz.csv","w")
    file.write(f"T{t}")
    file.close()

def is_it_darks():
    mpin=17
    tpin=27
    GPIO.setmode(GPIO.BCM)
    cap=0.000001
    adj=2.130620985
    i=0
    t=0
    GPIO.setwarnings(False)
    while True:
        GPIO.setup(mpin, GPIO.OUT)
        GPIO.setup(tpin, GPIO.OUT)
        GPIO.output(mpin, False)
        GPIO.output(tpin, False)
        time.sleep(0.2)
        GPIO.setup(mpin, GPIO.IN)
        time.sleep(0.2)
        GPIO.output(tpin, True)
        starttime=time.time()
        endtime=time.time()
        while (GPIO.input(mpin) == GPIO.LOW):
            endtime=time.time()
        measureresistance=endtime-starttime
        res=(measureresistance/cap)*adj
        i=i+1
        t=t+res
        if i==10:
                t=t/i
                if t>100:
                    sense.low_light = True
                    i=0
                    t=0
                    return
                elif t<=100:
                    sense.low_light = False
                    i=0
                    t=0
                    return
