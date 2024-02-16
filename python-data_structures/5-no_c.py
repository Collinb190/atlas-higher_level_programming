#!/usr/bin/python3
def no_c(my_string):
    remove = "cC"
    transTable = str.maketrans("", "", remove)
    newString = my_string.translate(transTable)
    return newString
