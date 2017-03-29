from __future__ import print_function

import sys
from csv import reader
from operator import add
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_amount_blanklines <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(lambda row: row[3] == '')
    counts = lines.map(lambda row : ('blank', 1)).reduceByKey(add).sortBy(lambda x: x[1], False)
    counts = counts.map(lambda x: str(x[1])+'\t'+x[0])
    counts.saveAsTextFile("amount_blanklines.out")
    sc.stop()
