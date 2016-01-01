#!/bin/bash

if [[ -z $1 ]]; then
	read -p "Enter the name of the new role: " role
else
	role=$1
fi
for i in files handlers tasks templates vars defaults meta; do mkdir -p roles/$role/$i; done
