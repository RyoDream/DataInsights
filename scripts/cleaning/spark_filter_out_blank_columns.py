from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext

indices = [1, 2, 5, 6, 7, 10, 13, 14]

def filter_out_blank(row):
    for index in indices:
        if row[index] == '':
            return False
    return True

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

def dump_csv2(row):
    line = ""
    for i in range(0, 24):
        if (i == 7 or i == 9 or i == 23) and row[i] != '':
            line += '\"'+row[i]+'\"'
        else:
            line += row[i]
        if i != 23:
            line += ','
    return line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_filter_out_blank_columns <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(filter_out_blank).map(dump_csv)
    lines.saveAsTextFile("filter_out_blank_columns.out")
    sc.stop()
