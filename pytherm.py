#!/usr/bin/python3

''' Starting script for all pyterm functionalities.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import os
import glob
import datetime
import time

from DS18B20 import DS18B20

base_dir = '/sys/bus/w1/devices/'
data_dir = '/mnt/pytherm-data/'
sensors_dirs = glob.glob(base_dir + '28*')
sensors = []
for item in sensors_dirs:
    sensors.append(DS18B20(item))


def record_sensors(interval):
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    data_filename = data_dir + datetime.now().strftime('%Y-%m-%d') + '.txt'

    if os.path.exists(data_filename):
        f = open(data_filename, 'a')
    else:
        f = open(data_filename, 'w')

    while True:
        for sensor in sensors:
            data_string = sensor.sensor_id + ',' + datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + \
                ',' + str(sensor.read_temp()) + '\n'
            f.write(data_string)
        time.sleep(interval)


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
    elif args.loop:
        while True:
            for sensor in sensors:
                print(sensor.sensor_id, ':', sensor.read_temp())
            time.sleep(1)
    elif args.record:
        record_sensors(args.record)
    else:
        for sensor in sensors:
            print(sensor.sensor_id, ':', sensor.read_temp())
