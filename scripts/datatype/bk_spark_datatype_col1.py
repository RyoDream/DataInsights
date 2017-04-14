from __future__ import print_function

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime

index = 1
semantic = 'starting date of the crime'
data_type = 'DATE'

def validate_col(row):
    date = row[index]
    # default value
    value = 'VALID'

    # check for null
    if date == '':
        value = 'NULL'
    else:
        try:
            # invalid format or invalid date value
            if date != datetime.strptime(date, "%m/%d/%Y").strftime("%m/%d/%Y"):
                raise ValueError
            # date before 2006 or later than 2015
            year = int(datetime.strptime(date, "%m/%d/%Y").strftime('%Y'))
            if year < 2006 or year > 2015:
                raise ValueError
        except ValueError:
            value = 'INVALID'
    return date + ' ' + data_type + ' ' + semantic + ' ' + value

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_datatype_col"+str(index)+" <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).map(validate_col)
    lines.saveAsTextFile("datatype_col"+str(index)+".out")
    sc.stop()
