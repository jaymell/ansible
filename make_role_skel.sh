#!/bin/bash

read -p "Enter the name of the new role: " role
mkdir roles/$role
for i in files handlers tasks templates vars; do mkdir roles/$role/$i; done
