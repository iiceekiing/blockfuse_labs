#!/bin/bash

sum_even=0
sum_odd=0

for (( num=1; num<=10; num++ ));
do

	if (( $num % 2 == 0 )); then
		sum_even=$((sum_even + num )) 	


	else 
		 sum_odd=$((sum_odd + num ))    
	fi
done

echo "calculating the sum of all even number: ..."
echo " "
echo "$sum_even is the sum of all the even numbers in range 1--10"

echo " "

echo "now calculating the sum of all odd numbers:......"
echo " "
echo "$sum_odd is the sum of all the odd number in range 1--10"

