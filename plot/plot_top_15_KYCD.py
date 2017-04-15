#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        width = rect.get_width()
        ax.text(width, rect.get_y()+height/2.0, '%d'%int(width), va='center', ha='right')

x_pos  = [0] * 15
crimes = []
kycd = []
with open('../output/crime_amount_each_KYCD.out','r') as file:
    plots = csv.reader(file, delimiter='\t')
    i = 0
    for row in plots:
        if i == 15:
            break
        crimes.insert(0, int(row[0]))
        kycd.insert(0, row[1])
        x_pos[i] = i+1
        i+=1

fig, ax = plt.subplots(figsize=(12,5))
rect = ax.barh(x_pos, crimes)
ax.set_yticks(x_pos)
ax.set_yticklabels(kycd)
ax.set_xlabel('Crime Amount')
plt.title('Crime Amount of the Top 15 KYCD (2006 - 2015)')
auto_label(rect)
fig.tight_layout()
# plt.show()
plt.savefig('../output/images/top_15_KYCD.png')
