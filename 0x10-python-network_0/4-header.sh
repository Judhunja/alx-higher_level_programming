#!/bin/bash
# takes in an URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s -H "X-School-User-Id: 98" -X GET "$1"