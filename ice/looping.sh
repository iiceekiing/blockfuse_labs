#!/bin/bash


#for (( i=1; i<=100; i++ )); do

for i in {1..100}; do
	if [[ $i -ge 30 && $i -le 40 ]]; then
		continue
	fi
	echo $i
done
