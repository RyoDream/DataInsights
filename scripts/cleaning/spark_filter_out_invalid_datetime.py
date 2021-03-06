from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime

def filter_out_invalid_datetime(row):
    start_date = row[1]
    start_time = row[2]
    end_date = row[3]
    end_time = row[4]

    if start_date != '':
        start_year = int(datetime.strptime(start_date, '%m/%d/%Y').strftime('%Y'))
        if start_year > 2015 or start_year < 2006:
            return False

    if end_date != '':
        end_year = int(datetime.strptime(end_date, '%m/%d/%Y').strftime('%Y'))
        if end_year > 2015 or end_year < 2006:
           return False

    if start_date == '' or end_date == '':
        return True

    if start_time == '' or end_time == '':
        return datetime.strptime(start_date, '%m/%d/%Y') <= datetime.strptime(end_date, '%m/%d/%Y')
    
    start_date = datetime.strptime(start_date+' '+start_time, '%m/%d/%Y %H:%M:%S')
    end_date = datetime.strptime(end_date+' '+end_time, '%m/%d/%Y %H:%M:%S')
    return start_date <= end_date

def dump_csv(row):
    line = ""
    for i in range(0, 24):
        if row[i] == '' or "," not in row[i]:
            line += row[i]
        else:
            line += '\"' + row[i] + '\"'
        if i != 23:
            line += ','
    return line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_filter_out_invalid_datetime <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(filter_out_invalid_datetime).map(dump_csv)
    lines.saveAsTextFile("filter_out_invalid_datetime.out")
    sc.stop()
