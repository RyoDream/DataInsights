#!/usr/bin/python
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

boroughs = ('manhattan', 'brooklyn', 'bronx', 'queens', 'staten')
colors = ('green', 'orange', 'yellow', 'pink', 'blue')

def auto_label(rects, index):
    for rect in rects:
        height = rect.get_height()
        width = rect.get_width()
        ax[index].text(width, rect.get_y()+height/2.0, '%d'%int(width), va='center', ha='right')

def read_file(borough):
    x_pos = [0] * 5
    crimes = []
    kycd = []
    with open('../output/crime_type_each_borough_'+borough+'.out','r') as file:
        plots = csv.reader(file, delimiter='\t')
        i = 0
        for row in plots:
            if i == 5:
                break
            crimes.insert(0, int(row[0]))
            kycd.insert(0, row[2])
            x_pos[i] = i+1
            i+=1
    return x_pos, crimes, kycd

fig, ax = plt.subplots(len(boroughs), 1, figsize=(10,12))
for i in xrange(len(boroughs)):
    x_pos, crimes, kycd = read_file(boroughs[i])
    rect = ax[i].barh(x_pos, crimes, color = colors[i])
    ax[i].set_yticks(x_pos)
    ax[i].set_yticklabels(kycd)
    ax[i].set_xlabel('Crime Amount In '+boroughs[i])
    ax[i].set_ylabel('Crime Type')
    auto_label(rect, i)

fig.tight_layout()
# plt.show()
plt.savefig('../output/images/top_5_crime_type_each_borough.png')
