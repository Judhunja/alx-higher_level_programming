#!/bin/bash
# This script takes in URL and displays all HTTP methods the server will accept
curl -s -X OPTIONS "$1"