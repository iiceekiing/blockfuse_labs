#!/bin/bash

execute=true
engine_on=false

echo "welcome to my car garage! pick any car of your choice and follow the options for a spin"


echo "Select any option below:  

start ---> to start your favorite car

stop ---> to turn off car when you're done

help ---> to get help operating your choice car smoothly

exit ---> to terminate this program"



while $execute;
do

read -p "choose any option  to cruise  your car: " option

if [[ $option == "start" && $engine_on == false ]];
then
	engine_on=true
	echo "Turning on Engine"
	echo "Engine is now ON!"


elif [[ $option == "stop" && $engine_on == true ]];
then
	echo "Turning of engine"
	echo "Engine has been turned off"
	$execute=false
fi
done
