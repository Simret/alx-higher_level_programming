#!/usr/bin/python3
"""Post request to passed url with email and display body as response"""


import requests
from sys import argv


if __name__ == "__main__":
    r = requests.post(argv[1], {'email': argv[2]})
    print(r.text)
