#!/bin/bash

if [ $# -ne 4 ]
then
	echo "usage: bash run_spark [category] [event-name] [input-file] [borough]"
	exit 1
fi

category=$1
event=$2
input=$3
borough=$4

/usr/bin/hadoop fs -rm -r ${event}_${borough}.out
rm ../../output/${event}_${borough}.out
rm -rf ../../output/out/$event_${borough}

spark-submit ../${category}/spark_${event}.py $input $borough
/usr/bin/hadoop fs -get ${event}_${borough}.out ../../output/out/${event}_${borough}
/usr/bin/hadoop fs -getmerge ${event}_${borough}.out ../../output/${event}_${borough}.out
