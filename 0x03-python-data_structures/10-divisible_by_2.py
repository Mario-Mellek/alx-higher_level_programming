#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = my_list.copy()
    for i in range(len(newList)):
        if newList[i] % 2 == 0:
            newList[i] = True
        else:
            newList[i] = False
    return newList
