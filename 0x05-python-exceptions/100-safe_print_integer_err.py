import sys


def safe_print_integer_err(value):
    try:
        print(value)
        return True
    except TypeError:
        print("Exception:", TypeError, file=sys.stderr)
        return False
