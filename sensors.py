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
from DS18B20 import *

db = None
try:
    db = sqlite3.connect(cfg.DB_FILE)
except Error as e:
    print(e)

sensors_dirs = glob.glob(cfg.BASE_DIR + '28*')
sensors = []
for item in sensors_dirs:
    sensors.append(DS18B20(item))
if not sensors:
    print('No sensor found on host system.')
else:
    print(sensors)

if db is not None:
    try:
        c = db.cursor()
        c.execute(cfg.SQL_INIT)
    except Error as e:
        print(e)


def db_write_temp(data):
    sql = ''' 
        INSERT INTO temp(timestamp,sensor1,sensor2)
        VALUES(?,?,?) '''
    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
    return cur.lastrowid


def record_sensors():
    while True:
        db_write_temp((datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
                       sensors[0].read_temp(),
                       sensors[1].read_temp()))
        time.sleep(cfg.RECORD_INTERVAL)


def read_last():
    sql = 'SELECT * FROM temp LIMIT 1'
    cur = db.cursor()
    cur.execute(sql)
    return cur.fetchall()[0]


def read_last_24h():
    sql = 'SELECT * FROM temp LIMIT 1440'
    cur = db.cursor()
    cur.execute(sql)
    return cur.fetchall()


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description='Reads output from DS18B20 temperature sensors. Check config.py for settings.')
    parser.add_argument(
        '-l', '--loop', help='print temp loop (1s interval)', action='store_true')
    parser.add_argument(
        '-r', '--record', help='record data to database', action='store_true')
    parser.add_argument(
        '-s', '--show', help='show records for the last 24h', action='store_true')

    args = parser.parse_args()

    if args.loop and args.record:
        print('Loop and record functions are exclusive to each other.')

    elif args.loop:
        while True:
            for sensor in sensors:
                print(sensor.sensor_id, ':', sensor.read_temp())
            time.sleep(1)

    elif args.record:
        record_sensors()

    elif args.show:
        read_last_24h()

    else:
        for sensor in sensors:
            print(sensor.sensor_id, ':', sensor.read_temp())
