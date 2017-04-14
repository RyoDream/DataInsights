#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

import sys
from csv import reader
from operator import add
from pyspark import SparkContext

def fetch_location(row):
    location = row[23]
    location = location[1:-1]
    return '"' + location + '"'

def filter_out_empty(row):
    return row[23] != 'undefined'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_fetch_location <file>", file=sys.stderr)
        exit(-1)

    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x))
    lines = lines.filter(filter_out_empty).map(fetch_location)
    lines.saveAsTextFile("fetch_location.out")
    sc.stop()
