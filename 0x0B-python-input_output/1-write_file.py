#!/usr/bin/python3
'''A function that writes and returns number of characters written'''


def write_file(filename="", text=""):
    '''Define function'''
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
        return len(text)
