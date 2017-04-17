#!/bin/bash

if [ $# -ne 3 ]
then
	echo "usage: bash run_type_borough [category] [event-name] [input-file]"
	exit 1
fi

category=$1
event=$2
input=$3

bash run_spark.sh $category $event $input
cat ../../output/crime_type_each_borough.out | grep MANHATTAN > ../../output/crime_type_each_borough_manhattan.out

cat ../../output/crime_type_each_borough.out | grep BROOKLYN > ../../output/crime_type_each_borough_brooklyn.out

cat ../../output/crime_type_each_borough.out | grep QUEENS > ../../output/crime_type_each_borough_queens.out

cat ../../output/crime_type_each_borough.out | grep BRONX > ../../output/crime_type_each_borough_bronx.out

cat ../../output/crime_type_each_borough.out | grep STATEN > ../../output/crime_type_each_borough_staten.out

