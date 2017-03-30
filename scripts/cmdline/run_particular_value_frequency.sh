#!/bin/bash

if [ $# -ne 5 ]
then
	echo "usage: bash run_particular_value_frequency [category] [event-name] [input-file] [target-column-number] [target-value]"
	exit 1
fi

category=$1
event=$2
input=$3
column_index=$4
value=$5
line=8
total_lines=`wc -l ../${category}/spark_${event}.py | awk '{print $1}'`
target_out="col_${column_index}_${value}_each_month"

rm ../../output/${target_out}.out
/usr/bin/hadoop fs -rm -r ${event}.out

head -$(($line-1)) ../${category}/spark_${event}.py > temp.py 
echo "target_column = $column_index" >> temp.py
echo "target_value = \"$value\"" >> temp.py
tail -$((${total_lines}-${line})) ../${category}/spark_${event}.py >> temp.py
spark-submit temp.py $input
/usr/bin/hadoop fs -get ${event}.out ../../output/out/${target_out}
/usr/bin/hadoop fs -getmerge ${event}.out ../../output/${target_out}.out

rm temp.py
