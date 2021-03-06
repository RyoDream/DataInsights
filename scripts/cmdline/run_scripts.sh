#!/bin/bash

dataset='cleared_dataset.csv'
#dataset='nypd_crime.csv'
#dataset='small_crime.csv'

# Crime amounts in each day
#bash run_spark.sh datetime crime_amount_each_day $dataset

# Crime amounts in each month
#bash run_spark.sh datetime crime_amount_each_month $dataset

# Crime amounts in each year
#bash run_spark.sh datetime crime_amount_each_year $dataset

# Crime amounts in each weekday
#bash run_spark.sh datetime crime_amount_each_weekday $dataset

# Crime amounts in each hour
#bash run_spark.sh datetime crime_amount_each_hour $dataset

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

# Crime type in each borough
#bash run_type_borough.sh locations crime_type_each_borough $dataset

# Crime amount in each borough in each year
bash run_spark_with_parameter.sh locations crime_amount_borough_each_year $dataset BROOKLYN
bash run_spark_with_parameter.sh locations crime_amount_borough_each_year $dataset MANHATTAN
bash run_spark_with_parameter.sh locations crime_amount_borough_each_year $dataset BRONX
bash run_spark_with_parameter.sh locations crime_amount_borough_each_year $dataset QUEENS
bash run_spark_with_parameter.sh locations crime_amount_borough_each_year $dataset 'STATEN'

# Fetch geolocation in each borough
#./run_fetch_location.sh locations fetch_location $dataset manhattan
#./run_fetch_location.sh locations fetch_location $dataset brooklyn
#./run_fetch_location.sh locations fetch_location $dataset queens
#./run_fetch_location.sh locations fetch_location $dataset bronx
#./run_fetch_location.sh locations fetch_location $dataset staten


# Count frequency for particular columns for each month
#bash run_spark.sh statistics count_columns_each_month $dataset

# Count particular column value for each month
#bash run_particular_value_frequency.sh datetime particular_value_each_month small_crime.csv 11 MISDEMEANOR

# Fetch gps location
#bash run_spark.sh locations fetch_location $dataset

