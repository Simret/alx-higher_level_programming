#!/usr/bin/python3
'''A function that reads file and prints it'''


def read_file(filename=""):
    '''Function definition'''
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
