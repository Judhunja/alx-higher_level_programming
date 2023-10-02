#!/bin/bash
#this script displays status code of passed url
curl -o /dev/null -w '%{http_code}' -ILs "$1"
