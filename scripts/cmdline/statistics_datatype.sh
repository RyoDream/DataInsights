#!/bin/bash

printf "Col\tValid\tInvalid\tNULL\n"
echo "----------------------------"

for i in {0..22}
do
	file="../../output/datatype_col"$i".out"
	valid=`cat $file | grep VALID | wc -l`
	invalid=`cat $file | grep INVALID | wc -l`
	null=`cat $file | grep NULL | wc -l`
	printf "%d\t%d\t%d\t%d\n" $i $valid $invalid $null
done
