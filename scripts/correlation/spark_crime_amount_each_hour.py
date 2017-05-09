from __future__ import print_function

import sys
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime

def format_date(date_str):
    crime_date = datetime.strptime(date_str, '%H:%M:%S')
    return crime_date.strftime('%H')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_crime_amount_each_hour.py <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).map(lambda row: row[2])
    counts = lines.map(format_date).map(lambda crime_date : (crime_date, 1)).reduceByKey(add)
    counts = counts.map(lambda row : row[0]+"\t"+str(row[1]))
    counts.saveAsTextFile("crime_amount_each_hour.out")
    sc.stop()
