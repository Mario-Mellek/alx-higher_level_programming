#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = dict()
    for i in a_dictionary:
        result[i] = a_dictionary[i] * 2
    return result
