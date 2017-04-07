#!/bin/bash

if [ $# -ne 4 ]
then
	echo "usage: bash run_filter_out_blank_columns [category] [event-name] [input-file] [col1,col2,col3..]"
	exit 1
fi

category=$1
event=$2
input=$3
column_index=$4
line=8
total_lines=`wc -l ../${category}/spark_${event}.py | awk '{print $1}'`
target_out="filter_out_blank_columns"

rm -rf ../../output/out/${target_out}
rm ../../output/${target_out}.csv
/usr/bin/hadoop fs -rm -r ${event}.out

head -$(($line-1)) ../${category}/spark_${event}.py > temp.py 
echo "indices = ["${column_index}"]" >> temp.py
tail -$((${total_lines}-${line})) ../${category}/spark_${event}.py >> temp.py
spark-submit temp.py $input
/usr/bin/hadoop fs -get ${event}.out ../../output/out/${target_out}
/usr/bin/hadoop fs -getmerge ${event}.out ../../output/${target_out}.csv

rm temp.py
