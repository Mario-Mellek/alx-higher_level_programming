#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary and value:
        keys = [i for i in a_dictionary if a_dictionary[i] == value]
        for key in keys:
            del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
