#!/usr/bin/python3
def multiple_returns(sentence):
    tup1 = ()
    tup2 = ()
    for i in sentence:
        if len(sentence) == 0:
            tup2 = None
            return tup2
        else:
            tup1 = len(sentence)
            tup2 = sentence[0]
    return tup1, tup2

