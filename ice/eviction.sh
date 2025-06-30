#!/bin/bash

read -p "please enter a directory name:  " dir

mkdir ./$dir

read -p "please enter a file name you wish to create inside the $dir directory: " file

touch ./$dir/$file

ls ./$dir


