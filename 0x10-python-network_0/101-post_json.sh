#!/bin/bash
#sends JSON post request to URL and displays reponse body
curl -X POST -s -H "Content-Type: application/json" -d @"$2" "$1"
