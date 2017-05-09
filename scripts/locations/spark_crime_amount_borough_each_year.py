from __future__ import print_function

import sys
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime

def format_date(date_str):
    crime_date = datetime.strptime(date_str, '%m/%d/%Y')
    return crime_date.strftime('%Y')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: spark_crime_amount_borough_each_year.py <file> <borough>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    borough = sys.argv[2]
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(lambda row: borough in row[13]).filter(lambda row: row[11] == 'FELONY').map(lambda row: row[1])
    counts = lines.map(format_date).map(lambda crime_date : (crime_date, 1)).reduceByKey(add)
    counts = counts.map(lambda row : row[0]+"\t"+str(row[1]))
    counts.saveAsTextFile("crime_amount_borough_each_year.out")
    sc.stop()
