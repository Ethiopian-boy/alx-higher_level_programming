#!/usr/bin/python3
def multiple_returns(sentence):
    multi = ()
    if len(sentence) == 0:
        multi = 0, "None"
    else:
        multi = len(sentence), sentence[0]
    return multi
