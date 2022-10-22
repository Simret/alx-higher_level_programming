#!/usr/bin/python3
"""Send a request to the url and display the values of the variable X-Request-Id"""


import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))