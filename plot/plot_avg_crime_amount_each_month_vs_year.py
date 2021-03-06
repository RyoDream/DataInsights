#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import calendar

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
		current_year.append(crime/days_in_month(int(date[i])))
		i+=1
	crimes_each_year.append(current_year)
	return crimes_each_year

def days_in_month(date):
	year = date/100
	month = date - year*100
	days = calendar.monthrange(year, month)
	return days[1]

crimes = fetch_crimes_each_year(crimes)
fig, ax = plt.subplots(figsize=(12,5))
ax.set_xticks(range(0, len(months)+1))
ax.set_xticklabels(months)

year = 2006
for crime in crimes:
	ax.plot(crime, label=year)
	year+=1

plt.xlabel('Crime Date')
plt.ylabel('Average Crime Amount per Day')
plt.title('Average Crime Amount Per Day In Each Month (2006 - 2015)')
plt.axis('auto')
plt.legend(loc=8)
plt.grid(True)
# plt.show()
plt.savefig('../output/images/avg_crimes_amount_each_month_vs_year.png')
