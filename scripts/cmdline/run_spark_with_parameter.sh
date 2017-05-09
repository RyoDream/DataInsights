#!/bin/bash

if [ $# -ne 4 ]
then
	echo "usage: bash run_spark [category] [event-name] [input-file] [parameter]"
	exit 1
fi

category=$1
event=$2
input=$3
parameter=$4

/usr/bin/hadoop fs -rm -r ${event}.out
rm ../../output/${event}.out
rm -rf ../../output/out/$event

spark-submit ../${category}/spark_${event}.py $input $parameter
/usr/bin/hadoop fs -get ${event}.out ../../output/out/$event

/usr/bin/hadoop fs -getmerge ${event}.out ../../output/unsort.out
sort -n ../../output/unsort.out > ../../output/${event}_${parameter}.out
rm ../../output/unsort.out
