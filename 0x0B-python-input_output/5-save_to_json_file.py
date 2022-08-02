#!/usr/bin/python3
'''A function with json representation written to file'''


import json


def save_to_json_file(my_obj, filename):
    '''function definition'''
    with open(filename, mode="w+") as f:
        json.dump(my_obj, f)i
