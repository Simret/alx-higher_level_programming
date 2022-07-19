#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    a = False
    msg = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(value))
        a = True
    except (ValueError, TypeError) as msg:
        print("Exception: {}".format(msg), file=sys.stderr)
    return a
