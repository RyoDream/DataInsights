from __future__ import print_function

import sys
from csv import reader
from operator import add
from pyspark import SparkContext


columns = {
        0: 'CMPLNT_NUM',
        1: 'CMPLNT_FR_DT',
        2: 'CMPLNT_FR_TM',
        3: 'CMPLNT_TO_DT',
        4: 'CMPLNT_TO_TM',
        5: 'RPT_DT',
        6: 'KY_CD',
        7: 'OFNS_DESC',
        8: 'PD_CD',
        9: 'PD_DESC',
        10: 'CRM_ATPT_CPTD_CD',
        11: 'LAW_CAT_CD',
        12: 'JURIS_DESC',
        13: 'BORO_NM',
        14: 'ADDR_PCT_CD',
        15: 'LOC_OF_OCCUR_DESC',
        16: 'PREM_TYP_DESC',
        17: 'PARKS_NM',
        18: 'HADEVELOPT',
        19: 'X_COORD_CD',
        20: 'Y_COORD_CD',
        21: 'Latitude',
        22: 'Longitude',
        23: 'Lat_Lon'
}

def filter_value(row):
    return row[target_column] == target_value

def parse_row(row):
    dateinfo = row[1].split('/')
    date = dateinfo[2]+' '+dateinfo[0]
    return columns[target_column]+' '+date+' '+row[target_column]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark_particular_value_each_month <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x : reader(x)).filter(filter_value).map(parse_row)
    counts = lines.map(lambda column : (column, 1)).reduceByKey(add).sortBy(lambda x: x[0], False)
    counts = counts.map(lambda x: x[0]+'\t'+str(x[1]))
    counts.saveAsTextFile("particular_value_each_month.out")
    sc.stop()
