#!/bin/bash

for file in `ls | grep py`
do
    python2 $file
    echo 'Running '$file
done
