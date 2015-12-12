#!/bin/bash

if [[ -z $1 ]]; then
	read -p "Enter the name of the new role: " role
else
	role=$1
fi
mkdir roles/$role
for i in files handlers tasks templates vars defaults; do mkdir roles/$role/$i; done
