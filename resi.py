# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:17:42 2023

@author: bb005584
"""

#import the GPIO and time package
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

for i in range(5):
    GPIO.output(29,True)
    time.sleep(1)
    GPIO.output(29,False)
    time.sleep(1)
    
    GPIO.output(31,True)
    time.sleep(1)
    GPIO.output(31,False)
    time.sleep(20)

GPIO.cleanup()