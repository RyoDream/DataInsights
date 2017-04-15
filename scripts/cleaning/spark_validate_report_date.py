from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime

def validate_date(row):
    start_date = row[1]
    report_date = row[5]
    if start_date == '' or report_date == '':
        return False
    
    start_date = datetime.strptime(start_date, '%m/%d/%Y')
    report_date = datetime.strptime(report_date, '%m/%d/%Y')
    report_year = int(start_date.strftime('%Y'))
    if report_year < 2006 or report_year > 2015 or start_date > report_date:
        return True

    end_date = row[3]
    if end_date != '':
        end_date = datetime.strptime(end_date, '%m/%d/%Y')
        if end_date > report_date:
            return True

    return False

def dump_csv(row):
    start_date = row[1] if row[1] != '' else 'NULL'
    end_date = row[3] if row[3] != '' else 'NULL'
    report_date = row[5] if row[5] != '' else 'NULL'
    crime_id = row[0]
    return crime_id+'\t'+start_date+'\t'+start_time+'\t'+end_date+'\t'+end_time

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
