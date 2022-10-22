#!/usr/bin/python3
"""Take github credentials and display id"""


import requests
from sys import argv


if __name__ == "__main__":
    uid = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2])).json()
    if "id" in uid:
        print(uid['id'])
    else:
        print(None)
