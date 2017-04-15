#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

month, crimes = np.loadtxt("../output/crime_amount_months.out", delimiter='\t', unpack=True)
months = ("Jan", "Feb", "Mar", "Apr", "May",
		  "June", "July", "Aug", "Sep", "Oct",
		  "Nov", "Dec")

def auto_label(rects):
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2.0, height, '%d'%int(height), ha='center', va='bottom')

# format the coordinators
fig, ax = plt.subplots(figsize=(10,5))
x_pos = np.arange(len(months))
rect = ax.bar(x_pos, crimes, color='green')
ax.set_xticks(x_pos)
ax.set_xticklabels(months)
ax.set_ylabel('Crime Amount')
ax.set_title('Crime Amount By Month')
auto_label(rect)
plt.plot(crimes, 'r')
# plt.show()
plt.savefig('../output/images/crimes_amount_month.png')
