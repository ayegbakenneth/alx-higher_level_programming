#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    ken = 0
    fred = None
    for t, c in a_dictionary.items():
        if c > ken:
            ken = c
            fred = t
    return fred
