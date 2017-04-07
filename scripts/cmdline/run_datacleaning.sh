#!/bin/bash

dataset='nypd_crime.csv'

# Filter out blank cells in particular columns
#bash run_filter_out_blank_columns.sh cleaning filter_out_blank_columns $dataset 1,2,5,6,7,10,13,14

#/usr/bin/hadoop fs -rm cleared_dataset.csv
#/usr/bin/hadoop fs -put ../../output/filter_out_blank_columns.csv cleared_dataset.csv

dataset='cleared_dataset.csv'
# Replace blank cells to 'undefined' in each columns
#bash run_replace_blank_columns.sh cleaning replace_blank_columns cleared_dataset.csv

#/usr/bin/hadoop fs -rm cleared_dataset.csv
#/usr/bin/hadoop fs -put ../../output/replace_blank_columns.csv cleared_dataset.csv

# Check if the key is duplicated
#bash run_spark.sh cleaning check_duplicate $dataset

# Count frequency in each value
bash run_count_frequency.sh cleaning count_frequency $dataset 6 18 8

# Validate format for particular column
# Validate CMPLNT_FR_TM
#bash run_validate_format.sh cleaning validate_format $dataset 2 '(2[0-3]|1[0-9]|0[0-9]|[^0-9][0-9]):([0-5][0-9]|[0-9]):([0-5][0-9]|[0-9])'

# Validate CMPLNT_TO_TM
#bash run_validate_format.sh cleaning validate_format $dataset 4 '(2[0-3]|1[0-9]|0[0-9]|[^0-9][0-9]):([0-5][0-9]|[0-9]):([0-5][0-9]|[0-9])'

# Validate CMPLNT_FR_DT
#bash run_validate_date.sh cleaning validate_date cleared_dataset.csv 1

# Validate CMPLNT_TO_DT
#bash run_validate_date.sh cleaning validate_date cleared_dataset.csv 3

# Validate RPT_DT
#bash run_validate_date.sh cleaning validate_date cleared_dataset.csv 5

