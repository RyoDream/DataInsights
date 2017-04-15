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

# format the coordinators
fig, ax = plt.subplots(figsize=(10,5))
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
# ax.xaxis.set_minor_formatter(monthFmt)
datemin = dt.date(2006, 1, 1)
datemax = dt.date(2016, 1, 1)
ax.set_xlim(datemin, datemax)
ax.grid(True)
# fig.autofmt_xdate()

plt.xlabel('Crime Date')
plt.ylabel('Crime Amount')
plt.title('Crime Amount In Each Month')
plt.axis('auto')
plt.legend()

date, crimes = np.loadtxt("../output/crime_amount_each_month.out", delimiter='\t', unpack=True)

dates = []
for year in range(2006, 2016):
    for month in range(1, 13):
        dates.append(dt.datetime(year=year, month=month, day=1))

plt.plot(dates, crimes)
# plt.show()
plt.savefig('../output/images/crimes_amount_each_month.png')
