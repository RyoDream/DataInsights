#!/bin/bash

dataset='nypd_crime.csv'
#dataset='small_crime.csv'

# Crime amounts in each day
#bash run_spark.sh datetime crime_amount_each_day $dataset

# Crime amounts in each month
#bash run_spark.sh datetime crime_amount_each_month $dataset

# Crime amounts in each year
#bash run_spark.sh datetime crime_amount_each_year $dataset

# Crime amounts in each year (without year information)
#bash run_spark.sh datetime crime_amount_months $dataset

# Crime amounts for each KY_CD (classification code)
#bash run_spark.sh statistics crime_amount_each_KYCD $dataset

# Crime amounts for each LAW_CAT_CD (offense level)
#bash run_spark.sh statistics crime_amount_each_offense_level $dataset

# Crime amounts at each BORO_NM (borough)
#bash run_spark.sh locations crime_amount_each_borough $dataset

# Crime amounts at each premises
#bash run_spark.sh locations crime_amount_premises $dataset

# Crime amounts at each precincts
#bash run_spark.sh locations crime_amount_each_precincts $dataset

# Blank lines in each column
#bash run_spark.sh cleaning amount_blanklines_columns $dataset

# Count frequency in each value
#bash run_count_frequency.sh cleaning count_frequency small_crime.csv 6 18 8

# Check if the key is duplicated
#bash run_spark.sh cleaning check_duplicate $dataset

# Count frequency for particular columns for each month
#bash run_spark.sh statistics count_columns_each_month $dataset

# Count particular column value for each month
#bash run_particular_value_frequency.sh datetime particular_value_each_month small_crime.csv 11 MISDEMEANOR

# Validate format for patitular column
#bash run_spark.sh cleaning validate_format $dataset

# Filter out blank cells in particular columns
#bash run_filter_out_blank_columns.sh cleaning filter_out_blank_columns $dataset 1,2,5,6,7,10,13,14

# Replace blank cells to 'undefined' in each columns
bash

