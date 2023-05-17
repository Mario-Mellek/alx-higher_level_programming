#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniqueList = set(my_list)
    for i in uniqueList:
        result += i
    return result
