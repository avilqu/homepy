#!/usr/bin/python3

''' Starting script for all pyterm functionalities.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import glob
import time
from DS18B20 import DS18B20

base_dir = '/sys/bus/w1/devices/'
sensors_dirs = glob.glob(base_dir + '28*')
sensors = []
for item in sensors_dirs:
    sensors.append(DS18B20(item))

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description='Reads output from DS18B20 temperature sensors.')
    parser.add_argument(
        '-l', '--loop', help='print temp loop (1s interval)', action='store_true')

    args = parser.parse_args()

    if args.loop:
        while True:
            for sensor in sensors:
                temp = sensor.print_temp()
                print(sensor.sensor_id, ':', temp)
                # sensor.print_temp()
                time.sleep(1)
    else:
        for sensor in sensors:
            temp = sensor.print_temp()
            print(sensor.sensor_id, ':', temp)
            # sensor.print_temp()
