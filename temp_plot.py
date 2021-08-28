#!/usr/bin/python3

''' Generate temperature plot with data in CSV file.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

import numpy as np
import csv
import seaborn as plt

import config as cfg


def generate_plot(date):
    x = []
    y1 = []
    y2 = []

    with open(f'{cfg.DATA_DIR}{date}.txt') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        data_count = 0
        for row in csv_reader:
            x.append(row[0])
            y1.append(row[1])
            y2.append(row[2])
            data_count += 1

    plt.plot(x, y1, color='red', label='sensor 1')
    plt.plot(x, y2, color='blue', label='sensor 2')
    plt.title('Pyplot playground')
    plt.legend(loc='upper right')
