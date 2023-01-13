#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    for i in (my_list):
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            copy = my_list.copy()
            copy[idx] = element
    for i in (copy):
        return copy
