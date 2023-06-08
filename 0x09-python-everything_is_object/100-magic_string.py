#!/usr/bin/python3
def magic_string():
    magic_string.attr = getattr(magic_string, 'attr', 0) + 1
    return ", ".join(["BestSchool"] * magic_string.attr)
