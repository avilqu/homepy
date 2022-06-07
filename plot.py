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

last_time = data[0][1]
last_1 = data[0][2]
last_2 = data[0][3]

for data_point in data:
    x.append(dt.datetime.strptime(data_point[1], '%Y-%m-%dT%H:%M:%S'))
    y1.append(data_point[3])
    y2.append(data_point[2])

fig = plt.figure()
ax = plt.axes()
plt.title(f'{last_time}: {last_1} - {last_2}')
ax.plot(x, y1)
ax.plot(x, y2)
# ax.set_ylim([0, 30])
ax.set_xlim([dt.datetime.now() - dt.timedelta(hours=12), dt.datetime.now()])
# ax.set_xlim([dt.datetime.now() - dt.timedelta(hours=6), dt.datetime.now()])

# mpld3.show()

# plot_file = open('/home/tan/dev/tempy/index.html', 'w')
plot_file = open('/home/pi/tempy/index.html', 'w')
plot_file.write(mpld3.fig_to_html(fig))
plot_file.close()
