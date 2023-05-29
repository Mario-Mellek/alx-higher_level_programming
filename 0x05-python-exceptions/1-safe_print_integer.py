#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    except Exception as e:
        return False
    return True
