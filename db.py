#!/usr/bin/python3

''' Contains all methods to interact with InfluxDB.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

from influxdb import InfluxDBClient

import config as cfg


class DB:

    def __init__(self):
        self.db = InfluxDBClient(host=cfg.DB_URL, port=cfg.DB_PORT)
        self.db.switch_database(cfg.DB_NAME)

    def write_data_points(self, data_points):
        print(data_points)
        self.db.write_points(data_points)
