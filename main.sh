#!/bin/bash
# main bash script file for starting and running servers etc..

main="src/main.py"

if [ -z "$1" ]; then
	python3 src/main.py
else
	if [ "$1" == "test" ]; then
		echo "running tests!"
		python3 -m unittest discover -s src
	else
		echo "wrong argument given, possible argmunets are:\n-test"
	fi
fi

