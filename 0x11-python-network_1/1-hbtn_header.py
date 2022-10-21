#!/usr/bin/python3
"""Send a request to a given url, display the value of X-Request-Id variable"""


import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as reply:
        print(reply.getheader('X-Request-Id'))
