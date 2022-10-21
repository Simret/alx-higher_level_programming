#!/usr/bin/python3
"""Send a request to url and display body of response"""


import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
from sys import argv


if __name__ == "__main__":
    rep = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(rep) as reply:
            print(reply.read().decode(encoding="utf-8"))
    except URLError as err:
        print("Error code: {}".format(err.code))
