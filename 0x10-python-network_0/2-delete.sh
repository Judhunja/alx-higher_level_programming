#!/bin/bash
# This script sends a DELETE request to the URL pased as the first argument and displays body of the response
curl -sL -X DELETE "$1"
