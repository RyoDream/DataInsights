#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%\n({v:d})'.format(p=pct, v=val)
    return my_autopct

premises = []
crimes = []
with open('../output/crime_amount_premises.out','r') as file:
    plots = csv.reader(file, delimiter='\t')
    for row in plots:
        crimes.append(int(row[0]))
        premises.append(row[1])

fig, ax = plt.subplots(figsize=(9,5))
ax.pie(crimes, labels=premises, autopct = '%3.1f%%',
        startangle=45, labeldistance = 1.1)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Crime Amount For Crime Location')
plt.legend(loc=2)
# plt.show()
plt.savefig('../output/images/crime_amount_premises.png')