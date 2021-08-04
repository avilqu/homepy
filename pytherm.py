''' Reads temperature from a DS18B20 sensor. Written for Raspberry Pi 4B.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
while True:
    temp = sensor.get_temperature()
    print('Temperature (C): ' + temp)
    time.sleep(1)
