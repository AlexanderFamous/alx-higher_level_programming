#!/usr/bin/python3
def multiple_returns(sentence):
    tup1 = ()
    length = len(sentence)
    if length == 0:
        first_c = None
    else:
        first_c = sentence[0]
    tup1 = (length, first_c)
    return tup1
