#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%\n({v:d})'.format(p=pct,v=val)
    return my_autopct



crimes = []
level = []
with open('../output/crime_amount_each_offense_level.out','r') as file:
    plots = csv.reader(file, delimiter='\t')
    for row in plots:
        crimes.append(int(row[0]))
        level.append(row[1])

fig, ax = plt.subplots()
ax.pie(crimes, labels=level, autopct=make_autopct(crimes),
        shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Crime Amount At Each Offense Level')
# plt.show()
plt.savefig('../output/images/crime_amount_each_offense_level.png')