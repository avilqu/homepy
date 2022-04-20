#!/usr/bin/python3

import datetime as dt
import matplotlib.pyplot as plt
import mpld3

import sensors

sample_length = 14400
data = sensors.read_last_x(sample_length)

x = []
y1 = []
y2 = []

for data_point in data:
    x.append(dt.datetime.strptime(data_point[1], '%Y-%m-%dT%H:%M:%S'))
    y1.append(data_point[2])
    y2.append(data_point[3])

fig = plt.figure()
ax = plt.axes()
ax.plot(x, y1)
ax.plot(x, y2)
ax.set_ylim([8, 35])
ax.set_xlim([dt.datetime.now() - dt.timedelta(days=1), dt.datetime.now()])

plot_file = open('index.html', 'w')
plot_file.write(mpld3.fig_to_html(fig))
plot_file.close()
