#!/usr/bin/python3
def best_score(a_dictionary):
    #value = a_dictionary.values()
    if not a_dictionary:
        return None
    else:
        max_value = max(a_dictionary, key =a_dictionary.get)
    return max_value

