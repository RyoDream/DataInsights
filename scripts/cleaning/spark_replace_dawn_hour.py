from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime
from datetime import timedelta

def replace_dawn_hour(row):
    for index in (2, 4):
        if row[index] == '24:00:00':
            row[index] = '00:00:00'
            crime_date = datetime.strptime(row[index-1], '%m/%d/%Y')
            crime_date += timedelta(days=1)
            row[index-1] = crime_date.strftime('%m/%d/%Y')
    return row

def dump_csv(row):
    line = ""
    for i in range(0, 24):
        if row[i] == '' or "," not in row[i]:
            line += row[i]
        else:
            line += '\"' + row[i] + '\"'
        if i != 23:
            line += ','
    return line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_replace_dawn_hour <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).map(replace_dawn_hour).map(dump_csv)
    lines.saveAsTextFile("replace_dawn_hour.out")
    sc.stop()
