from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime



def validate_date(row):
    date = row[index]
    if date == '' or date == 'undefined':
        return False

    try:
        if date != datetime.strptime(date, "%m/%d/%Y").strftime("%m/%d/%Y"):
            raise ValueError
        return False
    except ValueError:
        return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_validate_date <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(validate_date)
    lines = lines.map(lambda row : (row[0]+'   '+row[index]))
    lines.saveAsTextFile("validate_date.out")
    sc.stop()
