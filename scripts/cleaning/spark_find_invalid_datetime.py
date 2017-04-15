from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime

def find_invalid_datetime(row):
    start_date = row[1]
    start_time = row[2]
    end_date = row[3]
    end_time = row[4]
    if start_date == '' or end_date == '':
        return False
    if start_time == '' or end_time == '':
        return datetime.strptime(start_date, '%m/%d/%Y') > datetime.strptime(end_date, '%m/%d/%Y')
    
    start_date = datetime.strptime(start_date+' '+start_time, '%m/%d/%Y %H:%M:%S')
    end_date = datetime.strptime(end_date+' '+end_time, '%m/%d/%Y %H:%M:%S')
    return start_date >= end_date

def dump_csv(row):
    start_date = row[1]
    start_time = row[2]
    end_date = row[3]
    end_time = row[4]
    crime_id = row[0]
    return crime_id+' '+start_date+' '+start_time+' '+end_date+' '+end_time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_filter_out_by_year <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(find_invalid_datetime).map(dump_csv)
    lines.saveAsTextFile("find_invalid_datetime.out")
    sc.stop()
