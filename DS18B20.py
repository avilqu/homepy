#!/usr/bin/python3

''' Class for reading output of a DS18B20 temperature sensor from a Raspberry Pi.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import os
import time
from datetime import datetime


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
            return round(temp_c, 1)

    def print_temp(self):
        temp_c = self.read_temp()
        print(temp_c)

    def print_loop(self):
        while True:
            temp_c = self.read_temp()
            print(temp_c)
            time.sleep(1)

    def record_temp(self, data_dir, interval):
        record_dir = data_dir + self.sensor_id + '/'
        if not os.path.exists(record_dir):
            os.mkdir(record_dir)

        data_filename = record_dir + datetime.now().strftime('%Y-%m-%d') + '.txt'

        if os.path.exists(data_filename):
            f = open(data_filename, 'a')
        else:
            f = open(data_filename, 'w')

        while True:
            data_string = datetime.now().strftime('%Y-%m-%dT%H:%M:%S') + \
                ',' + str(self.read_temp()) + '\n'
            f.write(data_string)
            time.sleep(interval)
