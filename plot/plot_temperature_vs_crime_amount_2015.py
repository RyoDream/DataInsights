#!/usr/bin/python
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates

# define axis locator
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
days = mdates.DayLocator() # every day
monthFmt = mdates.DateFormatter('%m-%d')
dayFmt = mdates.DateFormatter('%d')

# load data
date, crimes = np.loadtxt("../output/crime_amount_each_day_2015.out", delimiter='\t', unpack=True)
w_date, temperature, humidity, wind_speed = np.loadtxt("../output/weather_average_by_day_2015.out", delimiter=', ', unpack=True)

datemin = dt.datetime(2015, 1, 1)
datemax = dt.datetime(2015, 12, 31)
dates = range(0, len(date))

# format the coordinators

fig, ax1 = plt.subplots(figsize=(10,5))
ax1.xaxis.set_major_locator(months)
ax1.xaxis.set_major_formatter(monthFmt)
ax1.xaxis.set_minor_locator(days)
ax1.set_xlim(datemin, datemax)
# ax.xaxis.set_minor_formatter(monthFmt)
datemin = dt.date(2006, 1, 1)
datemax = dt.date(2016, 1, 1)
ax1.set_xlim(datemin, datemax)
ax1.grid(True)
ax1.xaxis.set_ticks(np.arange(1, 366, 30.0))

ax1.set_ylabel('Crime Amount')
plt.title('Crime Amount vs Temperature In Each Day (2015)')
plt.axis('auto')
plt.legend()
ax1.plot(dates, crimes, 'r', label='Crime Amount')

ax2 = ax1.twinx()
ax2.set_ylabel('avg. Temperature (F)')
ax2.grid(True)
ax2.plot(dates, temperature, 'g', label='Temperature')

plt.xlabel('Crime Date')
# plt.show()
plt.savefig('../output/images/temperature_vs_crimes_amount_2015.png')
