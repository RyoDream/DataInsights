#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

weeks = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
index, crimes = np.loadtxt("../output/crime_amount_each_weekday.out", delimiter='\t', unpack=True, dtype=int)

def auto_label(rects):
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2.0, height, '%d'%int(height), ha='center', va='bottom')

# format the coordinators
fig, ax = plt.subplots(figsize=(10,5))
x_pos = np.arange(len(weeks))
rect = ax.bar(x_pos, crimes, color='green')
ax.set_xticks(x_pos)
ax.set_xticklabels(weeks)
ax.set_ylabel('Crime Amount')
ax.set_title('Crime Amount By Weekday')
auto_label(rect)
# plt.show()
plt.savefig('../output/images/crimes_amount_each_weekday.png')
