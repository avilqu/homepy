#!/usr/bin/python3

''' Reads temperature from a DS18B20 sensor. Written for Raspberry Pi 4B.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import time
from w1thermsensor import W1ThermSensor

# for sensor in W1ThermSensor.get_available_sensors():
#     print("Sensor %s has temperature %.2f" %
#           (sensor.id, sensor.get_temperature()))

local_sensor = W1ThermSensor('3c01d0752026')
remote_sensor = W1ThermSensor('3c01d075bfb0')

while True:
    local_temp = local_sensor.get_temperature()
    remote_temp = remote_sensor.get_temperature()
    print('Local (C): ' + str(local_temp))
    print('Remote (C): ' + str(remote_temp))
    time.sleep(1)
