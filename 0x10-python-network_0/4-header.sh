#!/bin/bash
# GET request with header var X-School-User-Id val 98
curl -s "$1" -X GET -H "X-School-User-Id:98"
