#!/usr/bin/python3

''' CLI tool for DS18B20 sensor driver.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import os
import glob
from datetime import datetime
import time
import sqlite3
from sqlite3 import Error

import config as cfg
from DB import *
from DS18B20 import *

sensors_dirs = glob.glob(cfg.BASE_DIR + '28*')
sensors = []
for item in sensors_dirs:
    sensors.append(DS18B20(item))
if not sensors:
    print('No sensor found on host system.')
else:
    print(sensors)


def start_recording():
    db = DB()
    while True:
        db.write_data_points([{
            'measurement': 'indoorTemp',
            'fields': {
                'temperature': sensors[0].read_temp()
            }
        }, {
            'measurement': 'outdoorTemp',
            'fields': {
                'temperature': sensors[1].read_temp()
            }
        }])

        time.sleep(cfg.RECORD_INTERVAL)


# def db_connect():
#     db = None
#     try:
#         db = sqlite3.connect(cfg.DB_FILE)
#     except Error as e:
#         print(e)
#     return db


# def db_write_temp(db, data):
#     sql = f'''
#         INSERT INTO {cfg.DB_TBNAME}(timestamp,sensor1,sensor2)
#         VALUES(?,?,?) '''
#     cur = db.cursor()
#     cur.execute(sql, data)
#     db.commit()
#     return cur.lastrowid


# def record_sensors():
#     while True:
#         db_write_temp(db_connect(), (datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
#                                      sensors[0].read_temp(),
#                                      sensors[1].read_temp()))
#         time.sleep(cfg.RECORD_INTERVAL)


# def read_last():
#     sql = f'SELECT * FROM {cfg.DB_TBNAME} ORDER BY ID DESC LIMIT 1'
#     cur = db_connect().cursor()
#     cur.execute(sql)
#     return cur.fetchall()[0]


# def read_last_x(x):
#     sql = f'SELECT * FROM {cfg.DB_TBNAME} ORDER BY ID DESC LIMIT :limit'
#     cur = db_connect().cursor()
#     cur.execute(sql, {'limit': x})
#     return cur.fetchall()


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description='Reads output from DS18B20 temperature sensors. Check config.py for settings.')
    parser.add_argument(
        '-l', '--loop', help='print temp loop (1s interval)', action='store_true')
    parser.add_argument(
        '-r', '--record', help='record data to database', action='store_true')
    parser.add_argument(
        '-s', '--show', nargs='?', const=1, type=int, help='show records for the last x data points')

    args = parser.parse_args()

    if args.loop and args.record:
        print('Loop and record functions are exclusive to each other.')
        exit()

    elif args.loop:
        while True:
            for sensor in sensors:
                print(sensor.sensor_id, ':', sensor.read_temp())
            time.sleep(1)

    elif args.record:
        start_recording()

    elif args.show:
        temp_data = read_last_x(args.show)
        for data_point in temp_data:
            print(data_point)

    else:
        for sensor in sensors:
            print(sensor.sensor_id, ':', sensor.read_temp())
