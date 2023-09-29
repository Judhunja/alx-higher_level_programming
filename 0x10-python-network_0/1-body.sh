#!/bin/bash
# This script takes in an URL, sends a GET request to that URL and displays the body of the response
curl -s -w "%{http_code}" "$1" | awk -v RS=200 '/200/ {print $2}'
