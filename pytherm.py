#!/usr/bin/python3

''' Reads temperature from a DS18B20 sensor. Written for Raspberry Pi 4B.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import time
from w1thermsensor import W1ThermSensor

for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

sensor_local = W1ThermSensor(Sensor.DS18B20, "00000588806a")
#while True:
#    temp = sensor.get_temperature()
#    print('Temperature (C): ' + str(temp))
#    time.sleep(1)
