#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or sentence == "":
        tupleA = (0, None)
    else:
        tupleA = (len(sentence), sentence[0])
    return tupleA
