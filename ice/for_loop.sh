#!/bin/bash


# echo "please enter your age to know if you're a tennager or an adult"

#read age

#if [ $age -ge 18 ]; then
#	echo "you are $age years old: Adult"

#else
#	echo "you are under 18: still a teen"
#fi


for i in {1..100}; do
    if [[ $i -ge 30 && $i -le 40 ]]; then
        continue
    fi
    echo $i
done




