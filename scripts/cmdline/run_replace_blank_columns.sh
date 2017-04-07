#!/bin/bash

if [ $# -ne 3 ]
then
	echo "usage: bash run_replace_blank_columns [category] [event-name] [input-file]"
	exit 1
fi

category=$1
event=$2
input=$3

rm -rf ../../output/out/${event}
rm ../../output/${event}.csv
/usr/bin/hadoop fs -rm -r ${event}.out

spark-submit ../${category}/spark_${event}.py $input
/usr/bin/hadoop fs -get ${event}.out ../../output/out/${event}
/usr/bin/hadoop fs -getmerge ${event}.out ../../output/${event}.csv

