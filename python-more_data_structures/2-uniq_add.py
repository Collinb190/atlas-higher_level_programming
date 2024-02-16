#!/usr/bin/python3
def uniq_add(my_list=[]):
    newSet = set()
    for num in my_list:
        newSet.add(num)
    return sum(newSet)
