#!/bin/bash
# Send a Json POST request
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
