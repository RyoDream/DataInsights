#!/bin/bash

if [ $# -ne 5 ]
then
	echo "usage: bash run_validate_format [category] [event-name] [input-file] [target-column-number] [target-pattern]"
	exit 1
fi

category=$1
event=$2
input=$3
column_index=$4
pattern=$5
line=9
total_lines=`wc -l ../${category}/spark_${event}.py | awk '{print $1}'`
target_out="validate_format_on_col_${column_index}"

rm ../../output/${target_out}.out
/usr/bin/hadoop fs -rm -r ${event}.out

head -$(($line-1)) ../${category}/spark_${event}.py > temp.py 
echo "index = $column_index" >> temp.py
echo "pattern = \"$pattern\"" >> temp.py
tail -$((${total_lines}-${line})) ../${category}/spark_${event}.py >> temp.py
spark-submit temp.py $input
/usr/bin/hadoop fs -get ${event}.out ../../output/out/${target_out}
/usr/bin/hadoop fs -getmerge ${event}.out ../../output/${target_out}.out
echo "On Column: "$column_index >> temp.out
echo "Pattern: "$pattern >> temp.out
echo "-----------------------------" >> temp.out
echo "Column      Contents" >> temp.out
cat temp.out ../../output/${target_out}.out > temp2.out
cp temp2.out ../../output/${target_out}.out

rm temp.py
rm temp.out temp2.out
