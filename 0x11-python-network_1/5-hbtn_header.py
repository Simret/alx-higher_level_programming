#!/usr/bin/python3
"""Send a request to the url, display the value of X-Request-Id variable"""


import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
