#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_ccs811

i2c = board.I2C()  # uses board.SCL and board.SDA
ccs811 = adafruit_ccs811.CCS811(i2c)

print("initializing co2 monitor")
# Wait for the sensor to be ready
while not ccs811.data_ready:
    pass
print("done")

def get_co2():
    return "{}".format(ccs811.eco2)
def get_tvoc():
    return "{}".format(ccs811.tvoc)


