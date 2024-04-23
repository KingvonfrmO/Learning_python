import sys


def safe_function(fct, *args):
    try:
        outcome = fct(*args)
    except BaseException as e:
        outcome = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return outcome