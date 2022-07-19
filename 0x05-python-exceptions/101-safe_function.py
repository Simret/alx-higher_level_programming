#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    a = 0
    b = 0
    try:
        a = fct(*args)
        b = 1
    except BaseException as y:
        print("Exception: {}".format(y), file=sys.stderr)
    if b == 1:
        return a
    else:
        return None
