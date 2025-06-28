#!/bin/bash


read -p "Create your username:  " username

read  -p "Create your password:  " pwd1

read  -p "Confirm password:  " pwd2


while true; do


if [[ $pwd1 == $pwd2 ]]; then
	echo "password confirmed!"
	echo " "
	echo "account created successfully!"
	echo " "
	echo "Welcome $username !"
	exit


elif [[ $pwd1 != $pwd2 ]]; then
	echo "wrong password, try again $username!"
	exit	


else
	echo "invalid input"
	break

fi

done
