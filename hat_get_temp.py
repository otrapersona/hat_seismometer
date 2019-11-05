# -*- coding: utf-8 -*-
from sys import argv
soy_un_argumentvariable = argv
from sense_hat import SenseHat
sense = SenseHat()
temp = sense.get_temperature()
print("Estamos a %s C" % temp)
