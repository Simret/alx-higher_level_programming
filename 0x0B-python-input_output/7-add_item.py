#!/usr/bin/python3
"""A function that adds arguments of a list and writes it to a file"""
from sys import argv
from os import stat, path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """Function defineition"""
    file = "add_item.json"
    if path.isfile(file) and stat(file).st_size != 0:
        av = load_from_json_file(file)
    else:
        av = []
    av.extend(argv[1:])
    save_to_json_file(av, file)


if __name__ == "__main__":
    main()
