#!/usr/bin/python3
"""This module is to find maximum list integer
"""
def max_integer(list=[]):
    """This function works by finding integer max of a list
        return none if list is empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    b = 1
    while b < len(list):
        if list[b] > result:
            result = list[b]
        b += 1
    return result
