#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def get_watered(channel):
    if GPIO.input(channel):
        watered = False
    else:
        watered = True


watered = get_watered(channel)
def coap():
    return "Thirsty!".encode("UTF-8") if not watered else "Satiated!".encode("UTF-8")


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, get_watered)  # assign function to GPIO PIN, Run function on change
