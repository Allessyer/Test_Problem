#!/bin/bash

filename=$1
output=$2

echo "script is running..."

mkdir $output

for i in `seq 10`
do
        word=$(cat $filename |tr '[:space:]' '[\n*]'| tr -d [:punct:] |  tr '[:upper:]' '[:lower:]' | sed '/^$/d' | sort | uniq -c | sort -nr | head -$i | tail -n 1 | awk '{print $2}')
        number=$(cat $filename |tr '[:space:]' '[\n*]'| tr -d [:punct:] |  tr '[:upper:]' '[:lower:]' | sed '/^$/d' | sort | uniq -c | sort -nr | head -$i | tail -n 1 | awk '{print $1}')
	mkdir "$word"_"$number"
	echo "Created directory '$word'_'$number'"
	mv "$word"_"$number" $output
done
