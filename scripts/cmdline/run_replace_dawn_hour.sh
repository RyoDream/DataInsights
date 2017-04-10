#!/bin/bash

if [ $# -ne 3 ]
then
	echo "usage: bash run_replace_dawn_hour [category] [event-name] [input-file]"
	exit 1
fi

category=$1
event=$2
input=$3
target_out="replace_dawn_hour"

rm -rf ../../output/out/${target_out}
rm ../../output/${target_out}.csv
/usr/bin/hadoop fs -rm -r ${event}.out

spark-submit ../${category}/spark_${event}.py $input
/usr/bin/hadoop fs -get ${event}.out ../../output/out/${target_out}
/usr/bin/hadoop fs -getmerge ${event}.out ../../output/${target_out}.csv

