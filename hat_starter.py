from sense_hat import SenseHat
import time
import os
sense = SenseHat()
quien_fue_el_ultimo_diganme_la_verdad = [0,0,0]
os.system("python3 /home/pi/hat_seismometer/rainbow.py")
while True:
    direccion = sense.stick.wait_for_event().direction
    accion = sense.stick.wait_for_event().action
    if direccion != 'middle' and quien_fue_el_ultimo_diganme_la_verdad[0] == 0:
        quien_fue_el_ultimo_diganme_la_verdad = [1,0,0]
        os.system("python3 /home/pi/hat_seismometer/hat_clear.py")
    elif direccion != 'middle' and quien_fue_el_ultimo_diganme_la_verdad[1] == 0:
        quien_fue_el_ultimo_diganme_la_verdad = [0,1,0]
        os.system("python3 /home/pi/hat_seismometer/rainbow.py")
    elif direccion == "middle" and accion == 'held' and quien_fue_el_ultimo_diganme_la_verdad[2] == 0:
        quien_fue_el_ultimo_diganme_la_verdad = [0,0,1]
        os.system("pkill -f rainbow")
        os.system("python3 /home/pi/hat_seismometer/hat_dog.py")
    time.sleep(.5)
