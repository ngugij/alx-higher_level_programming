#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as err:
        from sys import stderr
        print("Exception: {}".format(err), file=stderr)
        return (None)
