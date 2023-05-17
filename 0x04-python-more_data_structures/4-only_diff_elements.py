#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = set()
    for i in set_1.union(set_2):
        if i in set_1 and i in set_2:
            continue
        else:
            result.add(i)
    return result
