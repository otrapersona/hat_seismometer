from sense_hat import SenseHat
import time
import os
sense = SenseHat()
quien_fue_el_ultimo_diganme_la_verdad = '¯\_(ツ)_/¯'
sense.low_light = True

while True:
    time.sleep(.1)
    direccion = sense.stick.wait_for_event().direction
    accion = sense.stick.wait_for_event().action
    if direccion != 'middle' and accion == 'released' and quien_fue_el_ultimo_diganme_la_verdad != 'clear':
        print (direccion, accion)
        quien_fue_el_ultimo_diganme_la_verdad = 'clear'
        os.system("python3 /home/pi/hat/hat_clear.py")
    elif direccion == "middle" and accion == 'released' and quien_fue_el_ultimo_diganme_la_verdad != 'dog':
        print (direccion, accion)
        quien_fue_el_ultimo_diganme_la_verdad = 'dog'
        os.system("python3 /home/pi/hat/hat_dog.py")
    elif direccion != 'middle' and accion == 'released' and quien_fue_el_ultimo_diganme_la_verdad != 'leds':
        print (direccion, accion)
        sense.set_pixel(2, 2, 245, 0, 135)
        sense.set_pixel(2, 5, 245, 0, 135)
        sense.set_pixel(5, 2, 245, 0, 135)
        sense.set_pixel(5, 5, 245, 0, 135)
        quien_fue_el_ultimo_diganme_la_verdad = 'leds'
    

# and os.system('pgrep -fc "hat_dog.py"') < 1:

# while True:
#     for event in sense.stick.get_events():
#         print (event.direction)
#         if event.direction == "down" or event.direction == "left" or event.direction == "right" or event.direction == "middle" or event.action == "held":
#             os.system('pkill -f "hat_dog.py"')
#             os.system("python3 /home/pi/hat/hat_clear.py")
#         elif event.direction == "up":
#             os.system("python3 /home/pi/hat/hat_dog.py")
#         time.sleep(.1)

# while True:
#         direccion = sense.stick.wait_for_event().action
#         if direccion == 'left' or direccion == 'right' or direccion == 'down' or direccion == 'middle':
#             os.system('pkill -f "hat_dog.py"')
#             os.system("python3 /home/pi/hat/hat_clear.py")
#             print (direccion)
#         elif direccion == "up":
#             os.system("python3 /home/pi/hat/hat_dog.py")
#             print (direccion)
#         time.sleep(.1)