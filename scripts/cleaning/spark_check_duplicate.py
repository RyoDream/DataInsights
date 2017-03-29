from __future__ import print_function

import sys
from csv import reader
from operator import add
from pyspark import SparkContext

index = 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_check_duplicate <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x))
    counts = lines.map(lambda row : (row[index], 1)).reduceByKey(add).filter(lambda x: x[1] > 1)
    counts = counts.map(lambda x: 'duplicate: '+x[0]+'\t'+str(x[1]))
    counts.saveAsTextFile("check_duplicate.out")
    sc.stop()
