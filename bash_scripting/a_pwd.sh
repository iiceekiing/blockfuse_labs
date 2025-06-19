#!/bin/bash

echo -n "Enter your password: "
stty -echo
read password
stty echo
echo
echo "Password received!"

