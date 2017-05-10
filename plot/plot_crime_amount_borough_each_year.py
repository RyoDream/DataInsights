#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

date, crimes = np.loadtxt("../output/crime_all_amount_borough_each_year_BROOKLYN.out", delimiter='\t', unpack=True)

fig, ax = plt.subplots(figsize=(12,5))
ax.set_xticks(range(0, len(date)+1))
ax.set_xticklabels(date)

plt.xlabel('Crime Date')
plt.ylabel('Crime Amount')
plt.title('Crime Amount In Brooklyn Each Year (2006 - 2015)')
plt.axis('auto')
# plt.legend(loc=8)
plt.grid(True)
plt.plot(crimes, 'r')
# plt.show()
plt.savefig('../output/images/crimes_amount_brooklyn_each_year.png')
