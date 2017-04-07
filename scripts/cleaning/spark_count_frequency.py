from __future__ import print_function

import sys
from csv import reader
from operator import add
from pyspark import SparkContext

index = 2

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_count_frequency <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x))
    counts = lines.map(lambda row : (row[index], 1)).reduceByKey(add).sortBy(lambda x: x[1], False)
    counts = counts.map(lambda x: str(x[1])+'\t'+x[0])
    counts.saveAsTextFile("count_frequency.out")
    sc.stop()
