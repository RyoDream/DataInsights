#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

hours, crimes = np.loadtxt("../output/crime_amount_each_hour.out", delimiter='\t', unpack=True, dtype=int)

def auto_label(rects):
	for rect in rects:
		height = rect.get_height()
		ax.text(rect.get_x()+rect.get_width()/2.0, height, '%d'%int(height), ha='center', va='bottom', size='small')

# format the coordinators
fig, ax = plt.subplots(figsize=(15,5))
x_pos = np.arange(len(hours))
rect = ax.bar(x_pos, crimes, color='green')
ax.set_xticks(x_pos)
ax.set_xticklabels(hours)
ax.set_xlabel('Hours')
ax.set_ylabel('Crime Amount')
ax.set_title('Crime Amount By Hour')
auto_label(rect)
plt.plot(hours, crimes, 'r')
# plt.show()
plt.savefig('../output/images/crimes_amount_hour.png')
