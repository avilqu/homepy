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

    def __init__(self, sensor_dir):
        self.sensor_dir = sensor_dir
        self.sensor_id = sensor_dir[23:]
        self.w1_slave = sensor_dir + '/w1_slave'

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

    def print_loop(self):
        while True:
            temp_c = round(self.read_temp(), 1)
            print(temp_c)
            time.sleep(1)


sensors_dirs = glob.glob(base_dir + '28*')
sensors = []
for item in sensors_dirs:
    sensors.append(DS18B20(item))

sensors[0].print_loop()

# if __name__ == "__main__":

#     import argparse

#     parser = argparse.ArgumentParser(
#         description='Reads output from a DS18B20 temperature sensor.')
#     parser.add_argument(
#         '-i', '--id', help='sensor ID', type=str, dest='sensor_id')
#     parser.add_argument(
#         '-l', '--loop', help='print temp loop (1s interval)', action='store_true')

#     args = parser.parse_args()

#     if args.sensor_id:
#         DS18B20(args.sensor_id).print_loop()
