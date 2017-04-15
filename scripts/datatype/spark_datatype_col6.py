#!/usr/bin/env python
# encoding: utf-8

import sys
import re
from csv import reader
from operator import add
from pyspark import SparkContext
from datetime import datetime

def is_typeof_integer(x):
    try :
        x = int(x)
    except ValueError:
        return False
    return True

def is_typeof_float(x):
    try:
        x = float(x)
    except ValueError:
        return False
    return True

def is_typeof_date(x):
    try:
        x = datetime.strptime(x, '%m/%d/%Y')
    except ValueError:
        return False
    return True

def is_typeof_time(x):
    try:
        x = datetime.strptime(x, '%H:%M:%S')
    except ValueError:
        return False
    return True

def determine_type_of(x):
    if is_typeof_integer(x):
        return 'INTEGER'
    if is_typeof_float(x):
        return 'FLOAT'
    if is_typeof_date(x):
        return 'DATE'
    if is_typeof_time(x):
        return 'TIME'
    return 'TEXT'

def is_semantic_of_borough(x):
    boroughs = ('BROOKLYN', 'MANHATTAN', 'BRONX', 'QUEENS', 'STATEN ISLAND')
    return determine_type_of(x) == 'TEXT' and x in boroughs

def is_semantic_of_offense_level(x):
    offense_levels = ('FELONY', 'MISDEMEANOR', 'VIOLATION')
    return determine_type_of(x) == 'TEXT' and x in offense_levels

def is_semantic_of_premises(x):
    premises = ('INSIDE', 'FRONT OF', 'OPPOSITE OF', 'REAR OF', 'OUTSIDE')
    return determine_type_of(x) == 'TEXT' and x in premises

def is_semantic_of_crime_status(x):
    status = ('COMPLETED', 'ATTEMPTED')
    return determine_type_of(x) == 'TEXT' and x in status

def is_semantic_of_geolocation(x):
    reg = '^(\([-+]?\d{1,2}[.]\d+),\s*([-+]?\d{1,3}[.]\d+\))$'
    res = re.match(reg, x)
    return res is not None
    
def determine_semantic_of(x, dtype):
    if dtype == 'INTEGER':
        value = int(x)
        if value < 1000:
            return 'Crime Code'
        if value < 100000000:
            return 'Coordinate Code'
        if value > 100000000 and value < 999999999:
            return 'Compliant ID'
        return 'Non-sense Number'
    if dtype == 'FLOAT':
        return 'Latitude or Longitude'
    if dtype == 'DATE':
        return 'Crime Started Date'
    if dtype == 'TIME':
        return 'Crime Occurence Time'
    if dtype == 'TEXT':
        if is_semantic_of_borough(x):
            return 'Borough of the Crime'
        if is_semantic_of_premises(x):
            return 'Location of Occurrence'
        if is_semantic_of_crime_status(x):
            return 'Indicator of Crime Status'
        if is_semantic_of_offense_level(x):
            return 'Offense Level'
        if is_semantic_of_geolocation(x):
            return 'Geolocation Pair'
    return 'Plain Text'

def determine_value_of(x, dtype, dsemantic, base_type, base_semantic):
    # Check data type
    if x == '':
        return 'NULL'
    # Check data semantic
    if dtype != base_type or dsemantic != base_semantic:
        return 'INVALID'
    return 'VALID'

def get_metadata_of(x):
    base_type = 'INTEGER'
    base_semantic = 'Crime Code'

    if x == '':
       return ('%s %s \"%s\" %s' % (x, base_type, base_semantic, 'NULL'))

    dtype = determine_type_of(x)
    dsemantic = determine_semantic_of(x, dtype)
    dvalue = determine_value_of(x, dtype, dsemantic, base_type, base_semantic)
    return ('%s %s \"%s\" %s' % (x, dtype, dsemantic, dvalue))

if __name__ == "__main__":
    index = 6
    if len(sys.argv) != 2:
        print("Usage: spark_datatype_col"+str(index)+" <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).map(lambda x: x[index]).map(get_metadata_of)
    lines.saveAsTextFile("datatype_col"+str(index)+".out")
    sc.stop()

