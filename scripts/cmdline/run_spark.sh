#!/bin/bash

if [ $# -ne 3 ]
then
	echo "usage: bash run_spark [category] [event-name] [input-file]"
	exit 1
fi

category=$1
event=$2
input=$3

/usr/bin/hadoop fs -rm -r ${event}.out
rm ../../output/${event}.out
rm -rf ../../output/out/$event

spark-submit ../${category}/spark_${event}.py $input
/usr/bin/hadoop fs -get ${event}.out ../../output/out/$event

if [ $category = 'datetime' ]
then
	/usr/bin/hadoop fs -getmerge ${event}.out ../../output/unsort.out
	sort -n ../../output/unsort.out > ../../output/${event}.out
	rm ../../output/unsort.out
else
	/usr/bin/hadoop fs -getmerge ${event}.out ../../output/${event}.out
fi
