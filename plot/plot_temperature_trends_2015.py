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
days = mdates.DayLocator() # every day
monthFmt = mdates.DateFormatter('%m-%d')
dayFmt = mdates.DateFormatter('%d')

# load data
date, crimes = np.loadtxt("../output/crime_amount_each_day_2015.out", delimiter='\t', unpack=True)
w_date, temperature, humidity, wind_speed = np.loadtxt("../output/weather_average_by_day_2015.out", delimiter=', ', unpack=True)

amount_dict = {}
count_dict = {}
for i in range(0, len(date)):
	temper = round(temperature[i])
	if temper in amount_dict:
		amount_dict[temper] += crimes[i]
		count_dict[temper] += 1
	else:
		amount_dict[temper] = crimes[i]
		count_dict[temper] = 1

temper = []
crimes = []
for tem in amount_dict.keys():
	temper.append(tem)
	crimes.append(amount_dict.get(tem) / count_dict.get(tem))

# format the coordinators
fig, ax = plt.subplots(figsize=(10,5))

# ax.xaxis.set_minor_formatter(monthFmt)
ax.grid(True)
plt.title('Average Crime Amount vs Temperature (2015)')
plt.ylabel('Average Crime Amount')
plt.xlabel('Temperature (F)')
plt.axis('auto')

plt.plot(temper, crimes, label='crime amount')
plt.legend()

# plt.show()
plt.savefig('../output/images/temperature_trends_2015.png')
