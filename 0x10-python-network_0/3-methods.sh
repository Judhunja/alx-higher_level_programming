#!/bin/bash
# This script takes in URL and displays all HTTP methods the server will accept
curl -X OPTIONS -sI "$1" | grep -i 'allow' | cut -d ':' -f 2- | sed 's/^[[:space:]]*//;s/[[:space:]]*$//'
