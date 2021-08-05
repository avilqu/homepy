#!/usr/bin/python3

''' Reads temperature from a DS18B20 sensor. Written for Raspberry Pi 4B.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import glob
import time

base_dir = '/sys/bus/w1/devices/'
local_sensor_dir = glob.glob(base_dir + '28*')[0]
local_sensor = local_sensor_dir + '/w1_slave'


class DS18B20:
    ''' Contains output data from a DS18B20 temp sensor '''

    def __init__(self, sensor_id):
        self.id = sensor_id
        self.w1_slave = base_dir + '28-' + sensor_id

    def read_raw(self):
        f = open(self.w1_slave, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        data = self.read_raw()
        while data[0].strip()[-3:] != 'YES':
            data = self.read_raw()

        temp_position = data[1].find('t=')
        if temp_position != -1:
            temp_string = data[1][temp_position+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

    def print_temp(self):
        temp_c = self.read_temp()
        print(temp_c)

    def print_loop(self, interval):
        while True:
            temp_c = self.read_temp()
            print(temp_c)
            time.sleep(interval)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description='Reads output from a DS18B20 temperature sensor.')
    parser.add_argument(
        '-i', '--id', help='sensor ID', type=str, dest='sensor_id')

    args = parser.parse_args()

    if args.sensor_id:
        DS18B20(args.sensor_id).print_loop(1)
