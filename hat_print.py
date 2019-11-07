# -*- coding: utf-8 -*-
from sys import argv
soy_un_argumentvariable = argv
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message(soy_un_argumentvariable[1], text_colour=[245, 0, 135])
#print(soy_un_argumentvariable[1])
