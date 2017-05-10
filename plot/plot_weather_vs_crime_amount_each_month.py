#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates

# define axis locator
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y-%m')
monthFmt = mdates.DateFormatter('%m')

# load data
date, crimes = np.loadtxt("../output/crime_amount_each_month.out", delimiter='\t', unpack=True)
w_date, temperature, humidity, wind_speed = np.loadtxt("../output/weather_average.out", delimiter=', ', unpack=True)

dates = []
for year in range(2006, 2016):
    for month in range(1, 13):
        dates.append(dt.datetime(year=year, month=month, day=1))

# format the coordinators

# fig, ax = plt.subplots(figsize=(10,5))
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(411)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(yearsFmt)
ax1.xaxis.set_minor_locator(months)
# ax.xaxis.set_minor_formatter(monthFmt)
datemin = dt.date(2006, 1, 1)
datemax = dt.date(2016, 1, 1)
ax1.set_xlim(datemin, datemax)
ax1.grid(True)
# fig.autofmt_xdate()

ax1.set_ylabel('Crime Amount')
plt.title('Crime Amount vs Weather In Each Month')
plt.axis('auto')
plt.legend()
ax1.plot(dates, crimes)

ax2 = fig.add_subplot(412, sharex=ax1)
ax2.set_ylabel('avg. temperature (F)')
ax2.grid(True)
ax2.plot(dates, temperature, 'r')

ax3 = fig.add_subplot(413, sharex=ax1)
ax3.set_ylabel('avg. humidity (%)')
ax3.grid(True)
ax3.plot(dates, humidity, 'g')

ax4 = fig.add_subplot(414, sharex=ax1)
ax4.set_ylabel('avg. Wind Speed (kn)')
ax4.grid(True)
ax4.plot(dates, wind_speed, 'b')

plt.xlabel('Crime Date')
# plt.show()
plt.savefig('../output/images/weather_vs_crimes_amount_each_month.png')
