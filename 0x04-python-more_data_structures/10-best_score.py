#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxVal = max(a_dictionary.values())
        maxKeys = [key for key, value in a_dictionary.items()
                   if value == maxVal]
        if len(maxKeys) > 1:
            return maxKeys
        elif len(maxKeys) == 1:
            return maxKeys[0]
    else:
        return None
