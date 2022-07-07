#!/bin/bash

cat dracula.txt |tr '[:space:]' '[\n*]'| tr -d [:punct:] |  tr '[:upper:]' '[:lower:]' | sed '/^$/d' | sort | uniq -c | sort -n 
