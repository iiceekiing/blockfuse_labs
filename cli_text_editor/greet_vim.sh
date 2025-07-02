#!/bin/bash


read -p "Please enter your name:  
" name

echo  "Welcome $name, how are you doing today ?"

read hwu


if [[ $hwu == "i'm fine" || $hwu == "fine" || $hwu == "okay" || $hwu == "doing good" || $hwu == "i am doing fine" || $hwu == "i am good" || $hwu == "good" || $hwu == "fantastic!" || $hwu == "all good!" ]]; then
	echo "good to hear you are fine $name"
	echo " "
	echo "feel free to reach out if you need any assistance with your tasks"
	  echo " "
	echo "good bye! $name, see you soon."

else
	echo "hope you are fine ? $name"
	echo " "
	echo "feel free to reach out if you need any assistance with your tasks"
	echo "good bye! $name, see you soon."
fi

