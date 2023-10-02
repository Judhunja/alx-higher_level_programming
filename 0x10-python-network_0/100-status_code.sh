#!/bin/bash
#this script displays status code of passed url
curl -sI "$1" | awk -F' ' 'NR==1 {print $2}'

