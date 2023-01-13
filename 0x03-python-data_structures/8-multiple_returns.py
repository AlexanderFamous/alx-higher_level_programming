#!/usr/bin/python3
def multiple_returns(sentence):
    tup1 = ()
    tup2 = ()
    length = len(sentence)
    for i in sentence:
        if length == 0:
            tup2 = None
        else:
            tup1 = len(sentence)
            tup2 = sentence[0]
    return tup1, tup2
