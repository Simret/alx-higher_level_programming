#!/usr/bin/python3
def safe_print_division(x, y):
    res = 0
    try:
        res = x / y
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
        return (res)
