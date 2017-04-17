#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import sys
from csv import reader
from operator import add
from pyspark import SparkContext

borough = sys.argv[2]

def fetch_location(row):
    return row[21] + '\t' + row[22]

def filter_borough(row):
    return borough.upper() in row[13] and row[21] != 'UNDEFINED' and row[22] != 'UNDEFINED'

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: spark_fetch_location <file> <borough name>", file=sys.stderr)
        exit(-1)

    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x))
    lines = lines.filter(filter_borough).map(fetch_location)
    lines.saveAsTextFile("fetch_location_"+borough+".out")
    sc.stop()
