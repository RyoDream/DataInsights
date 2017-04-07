from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext



def validate_format(row):
    date = row[index]
    return date != '' and date != 'undefined' and re.match(pattern, date) is None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_validate_format <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(validate_format)
    lines = lines.map(lambda row : (row[0]+'   '+row[index]))
    lines.saveAsTextFile("validate_format.out")
    sc.stop()
