from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext

def replace_blank(row):
    for index in range(0, 24):
        if row[index] == '':
            row[index] = 'UNDEFINED'
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
        print("Usage: spark_replace_blank_columns <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).map(replace_blank).map(dump_csv)
    lines.saveAsTextFile("replace_blank_columns.out")
    sc.stop()
