#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates

months = ("Jan", "Feb", "Mar", "Apr", "May",
		  "June", "July", "Aug", "Sep", "Oct",
		  "Nov", "Dec")

date, crimes = np.loadtxt("../output/crime_amount_each_month.out", delimiter='\t', unpack=True)

def fetch_crimes_each_year(crimes):
	i = 0
	crimes_each_year = []
	current_year = []
	for crime in crimes:
		if i != 0 and i%12 == 0:
			crimes_each_year.append(current_year)
			current_year = []
		current_year.append(crime)
		i+=1
	crimes_each_year.append(current_year)
	return crimes_each_year

crimes = fetch_crimes_each_year(crimes)
fig, ax = plt.subplots(figsize=(12,5))
ax.set_xticks(range(0, len(months)+1))
ax.set_xticklabels(months)

year = 2006
for crime in crimes:
	ax.plot(crime, label=year)
	year+=1

plt.xlabel('Crime Date')
plt.ylabel('Crime Amount')
plt.title('Crime Amount In Each Month (2006 - 2015)')
plt.axis('auto')
plt.legend(loc=8)
plt.grid(True)
# plt.show()
plt.savefig('../output/images/crimes_amount_each_month_vs_year.png')
