#!/bin/bash


#num=1

#while [[ $num -le 100 ]]; do
#	echo $num

#	num=$((num+1))


#	(( num+= 1 ))
# done



#num=100

#while [[ $num -ge 1 ]]; do
#	 echo $num
#	((num-= 1 ))












num=4

while [[ $num -le 100 ]]; do
	if [[ $num%2 == 0 ]]; then
		(( num+= 1 ))
		echo $num
	fi
	
done






