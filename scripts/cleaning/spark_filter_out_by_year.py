from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime

def filter_out_by_year(row):
    crime_date = datetime.strptime(row[1], '%m/%d/%Y')
    return int(crime_date.strftime('%Y')) >= 2006

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
        print("Usage: spark_filter_out_by_year <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(filter_out_by_year).map(dump_csv)
    lines.saveAsTextFile("filter_out_by_year.out")
    sc.stop()
