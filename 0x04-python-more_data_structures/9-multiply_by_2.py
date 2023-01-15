#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = a_dictionary.copy()
    new_list.update((key, value * 2) for key, value in new_list.items())
    return new_list
