#!/bin/bash

echo "Welcome to Ekuke Foundation Academy"

echo "Need help navigating? type 'help' for directives"

read -p "input your name to continue:  
"  username

while true; do


read -p "Please enter score:  
 " score

if [[ $score == exit  ]]; then
	echo "Good Bye! $username"
	break


elif [[ $score == help ]]; then
	echo "input a score to get your grade"
	echo "type 'exit'to terminate program"


#checking if users input is a number.

elif !  [[  $score =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
	echo "Invalid input!. Score must be a number"

#elif ! [[ $score =~ (\. ^[0-9]+$ ]]; then
#	echo "ekuke"

#checking if user inputs numbers less than 0 or gt 100

elif [[ $score -lt 0 || $score -gt 100 ]]; then
	echo "Error! score must be within the range of '0 -> 100'"


elif [[ $score -ge 70 && $score -le 100 ]]; then
	echo "grade: A
	Execellent result"

elif [[ $score -ge 60 && $score -le 69 ]]; then
	echo "grade:  B
	Good result"

elif [[ $score -ge 50 && $score -lt 60 ]]; then
	echo "grade: C
	Average result"

elif [[ $score -ge 40 && $score -lt 50 ]]; then
	echo "grade: D
	Poor performance"

elif [[ $score -ge 30 && $score -le 39 ]]; then
	echo "grade: E
	Very poor performance"

elif [[ $score -ge 0 && $score -le 29 ]]; then
	echo "grade: F
	please $username, consider changing carrier!"

else
	echo "unexpexted error! please try again"
fi
done
