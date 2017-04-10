#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import calendar

month, crimes = np.loadtxt("../output/crime_amount_months.out", delimiter='\t', unpack=True)
months = ("Jan", "Feb", "Mar", "Apr", "May",
		  "June", "July", "Aug", "Sep", "Oct",
		  "Nov", "Dec")

def auto_label(rects):
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2.0, height, '%.2f'%height, ha='center', va='bottom')

def total_days_each_month():
	days = [0]*12
	for year in range(2006, 2016):
		for month in range(1, 13):
			days[month-1] += calendar.monthrange(year, month)[1]
	return days

def average_crimes_each_month(crimes):
	days = total_days_each_month()
	for i in xrange(0, 12):
		crimes[i] /= (1.0*days[i])
	return crimes

# format the coordinators
crimes = average_crimes_each_month(crimes)

fig, ax = plt.subplots(figsize=(10, 5))
x_pos = np.arange(len(months))
rect = ax.bar(x_pos, crimes, color='green')
ax.set_xticks(x_pos)
ax.set_xticklabels(months)
ax.set_ylabel('Crime Amount')
ax.set_title('Average Crime Amount Per Day By Month (2006 - 2015)')
auto_label(rect)
# plt.show()
plt.savefig('../output/images/avg_crimes_amount_month.png')
