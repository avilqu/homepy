#!/usr/bin/python3

''' DS18B20 temperature sensor driver.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''


class DS18B20:

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
