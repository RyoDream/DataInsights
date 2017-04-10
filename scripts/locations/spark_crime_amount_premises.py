from __future__ import print_function

import sys
from csv import reader
from operator import add
from pyspark import SparkContext

def filter_empty(row):
    return row[15] != '' and row[15] != 'undefined'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_crime_amount_premises <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(filter_empty)
    counts = lines.map(lambda row : (row[15], 1)).reduceByKey(add).sortBy(lambda x: x[1], False)
    counts = counts.map(lambda x: str(x[1])+'\t'+x[0])
    counts.saveAsTextFile("crime_amount_premises.out")
    sc.stop()
