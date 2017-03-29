#!/bin/bash

if [ $# -ne 6 ]
then
	echo "usage: bash run_spark [category] [event-name] [input-file]"
	exit 1
fi

category=$1
event=$2
input=$3
begin=$4
end=$5
line=$6
total_lines=`wc -l ../${category}/spark_${event}.py | awk '{print $1}'`

rm ../../output/${event}.out

while [ $begin -le $end ]
do
	head -$(($line-1)) ../${category}/spark_${event}.py > temp.py 
	echo 'index = '$begin >> temp.py
	tail -$((${total_lines}-${line})) ../${category}/spark_${event}.py >> temp.py
	begin=$(($begin+1))
	/usr/bin/hadoop fs -rm -r ${event}.out 
	spark-submit temp.py $input
	echo "For Column $begin ------------------------------------" >> ../../output/${event}.out
	echo "Count   Value" >> ../../output/${event}.out
	/usr/bin/hadoop fs -getmerge ${event}.out temp.out
	cat temp.out >> ../../output/${event}.out
	echo " " >> ../../output/${event}.out
done

rm temp.py
