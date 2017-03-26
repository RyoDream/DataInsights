#!/bin/bash

dataset='small_crime.csv'

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
bash run_spark.sh locations crime_amount_each_precincts $dataset


