#!/usr/bin/python
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except Exception as y:
        print("Exception: {}".format(y), file=sys.stderr)
        return None
