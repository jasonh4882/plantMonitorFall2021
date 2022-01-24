#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Button = 26

GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_light():
    button_state = GPIO.input(Button)
    if button_state == 0:
        return "Light".encode("UTF-8")
    else:
        return "Dark".encode("UTF-8")
