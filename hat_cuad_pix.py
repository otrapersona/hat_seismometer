from sense_hat import SenseHat
sense = SenseHat()
import time
sense.low_light = True
sense.set_pixel(3, 3, 245, 0, 135)
sense.set_pixel(3, 4, 245, 0, 135)
sense.set_pixel(4, 3, 245, 0, 135)
sense.set_pixel(4, 4, 245, 0, 135)
time.sleep(.05)
sense.low_light = False
sense.clear()
