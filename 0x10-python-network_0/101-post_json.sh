#!/bin/bash
# Takes filename and URL, post contents of file; Usage: ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
