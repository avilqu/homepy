#!/usr/bin/python3

''' Starting script for all pyterm functionalities.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import glob
import time
import asyncio
from DS18B20 import DS18B20

base_dir = '/sys/bus/w1/devices/'
data_dir = '/mnt/pytherm-data/'
sensors_dirs = glob.glob(base_dir + '28*')
sensors = []
for item in sensors_dirs:
    sensors.append(DS18B20(item))


async def record_sensors(interval):
    for sensor in sensors:
        sensor.record_temp(data_dir, interval)

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description='Reads output from DS18B20 temperature sensors.')
    parser.add_argument(
        '-l', '--loop', help='print temp loop (1s interval)', action='store_true')
    parser.add_argument(
        '-r', '--record', help='record data to file with specified interval (in seconds)', type=int, dest='record')

    args = parser.parse_args()

    if args.loop and args.record:
        print('Loop and record functions are exclusive to each other.')

    if args.loop:
        while True:
            for sensor in sensors:
                print(sensor.sensor_id, ':', sensor.read_temp())
            time.sleep(1)
    elif args.record:
        asyncio.run(record_sensors(args.record))
    else:
        for sensor in sensors:
            print(sensor.sensor_id, ':', sensor.read_temp())
