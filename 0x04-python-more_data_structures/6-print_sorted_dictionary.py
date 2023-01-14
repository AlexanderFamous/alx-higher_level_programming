#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = a_dictionary.keys()
    sort_dic = sorted(sort_dic)
    for i in sort_dic:
        print("{}: {}".format(i, a_dictionary[i]))
