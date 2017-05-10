#!/bin/bash

bash run_spark.sh correlation weather_average_by_day weather.csv
bash run_spark.sh correlation weather_average_by_month weather.csv
bash run_spark.sh correlation weather_average_by_year  weather.csv




