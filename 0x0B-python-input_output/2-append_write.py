#!/usr/bin/python3
'''A function that appends characters & returns length of characters appended'''


def append_write(filename="", text=""):
    '''Define a function'''
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(text)
        return len(text)
